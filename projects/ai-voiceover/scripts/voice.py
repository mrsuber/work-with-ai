#!/usr/bin/env python3
"""
Voice cloning + text-to-speech CLI on top of the ElevenLabs API.

Two cloning modes:
  - Instant (ivc-create): fast, works from a few minutes of clean audio.
    Good for getting a usable clone immediately.
  - Professional (pvc-create / pvc-add-samples / pvc-train): higher
    fidelity, and explicitly designed to improve as you add more samples
    over time -- add new recordings to samples/, run pvc-add-samples, then
    pvc-train again whenever you want it to re-learn from everything so far.
    Requires a one-time identity verification (ElevenLabs' anti-abuse
    safeguard, done through their dashboard) before it can be used.

Usage:
  python voice.py ivc-create --name "My Voice"
  python voice.py pvc-create --name "My Voice" --language en
  python voice.py pvc-add-samples --voice-id <id>
  python voice.py pvc-train --voice-id <id>
  python voice.py generate --voice-id <id> --text "Hello there"
  python voice.py generate --voice-id <id> --text-file transcript.txt --out output/scene3.mp3
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv, set_key
from elevenlabs.client import ElevenLabs

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
SAMPLES_DIR = ROOT / "samples"
OUTPUT_DIR = ROOT / "output"
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".flac", ".ogg"}

load_dotenv(ENV_PATH)


def client():
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key or api_key == "your-api-key-here":
        sys.exit(
            f"ELEVENLABS_API_KEY not set. Copy .env.example to .env "
            f"({ENV_PATH}) and fill in your API key from "
            f"https://elevenlabs.io/app/settings/api-keys"
        )
    return ElevenLabs(api_key=api_key)


def sample_files():
    files = sorted(p for p in SAMPLES_DIR.iterdir() if p.suffix.lower() in AUDIO_EXTS)
    if not files:
        sys.exit(
            f"No audio files found in {SAMPLES_DIR}. Drop your voice "
            f"recordings there first (mp3/wav/m4a/flac/ogg)."
        )
    return files


def save_voice_id(voice_id: str):
    ENV_PATH.touch(exist_ok=True)
    set_key(str(ENV_PATH), "ELEVENLABS_VOICE_ID", voice_id)
    print(f"Saved ELEVENLABS_VOICE_ID={voice_id} to {ENV_PATH}")


def cmd_ivc_create(args):
    c = client()
    files = sample_files()
    print(f"Uploading {len(files)} file(s) for instant voice clone '{args.name}'...")
    result = c.voices.ivc.create(
        name=args.name,
        files=[str(f) for f in files],
        remove_background_noise=True,
    )
    print(f"Created voice_id: {result.voice_id}")
    save_voice_id(result.voice_id)


def cmd_pvc_create(args):
    c = client()
    result = c.voices.pvc.create(name=args.name, language=args.language)
    print(f"Created professional voice_id: {result.voice_id}")
    print(
        "Next: ElevenLabs requires a one-time identity verification for "
        "professional clones before training -- do that in the dashboard "
        f"(https://elevenlabs.io/app/voice-lab) for voice_id {result.voice_id}, "
        "then run pvc-add-samples and pvc-train."
    )
    save_voice_id(result.voice_id)


def cmd_pvc_add_samples(args):
    c = client()
    files = sample_files()
    print(f"Uploading {len(files)} file(s) to professional voice {args.voice_id}...")
    result = c.voices.pvc.samples.create(
        voice_id=args.voice_id,
        files=[str(f) for f in files],
        remove_background_noise=True,
    )
    print(f"Uploaded {len(result)} sample(s). Run pvc-train next to have it learn from these.")


def cmd_pvc_train(args):
    c = client()
    print(f"Starting training for voice {args.voice_id}...")
    c.voices.pvc.train(voice_id=args.voice_id)
    print("Training kicked off. Check status in the ElevenLabs dashboard -- "
          "training is asynchronous and can take a while depending on how "
          "much audio has been added.")


def cmd_generate(args):
    c = client()
    voice_id = args.voice_id or os.environ.get("ELEVENLABS_VOICE_ID")
    if not voice_id:
        sys.exit("No --voice-id given and ELEVENLABS_VOICE_ID not set in .env")

    if args.text_file:
        text = Path(args.text_file).read_text().strip()
    else:
        text = args.text
    if not text:
        sys.exit("Provide --text or --text-file")

    out_path = Path(args.out) if args.out else (OUTPUT_DIR / "voiceover.mp3")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating voiceover ({len(text)} chars) with voice {voice_id}...")
    audio = c.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id=args.model,
        output_format="mp3_44100_128",
    )
    with open(out_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"Wrote {out_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("ivc-create", help="Instant voice clone from samples/")
    p.add_argument("--name", required=True)
    p.set_defaults(func=cmd_ivc_create)

    p = sub.add_parser("pvc-create", help="Create an (empty) professional voice clone")
    p.add_argument("--name", required=True)
    p.add_argument("--language", default="en")
    p.set_defaults(func=cmd_pvc_create)

    p = sub.add_parser("pvc-add-samples", help="Add samples/ audio to an existing professional voice")
    p.add_argument("--voice-id", required=True)
    p.set_defaults(func=cmd_pvc_add_samples)

    p = sub.add_parser("pvc-train", help="(Re-)train a professional voice on all samples added so far")
    p.add_argument("--voice-id", required=True)
    p.set_defaults(func=cmd_pvc_train)

    p = sub.add_parser("generate", help="Generate a voiceover from text")
    p.add_argument("--voice-id", help="Defaults to ELEVENLABS_VOICE_ID in .env")
    p.add_argument("--text")
    p.add_argument("--text-file")
    p.add_argument("--out")
    p.add_argument("--model", default="eleven_multilingual_v2")
    p.set_defaults(func=cmd_generate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
