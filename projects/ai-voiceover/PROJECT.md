# AI Voiceover (voice clone)

## Purpose

Clone the user's own voice so that, given a transcript, a voiceover can be
generated in that voice — good enough that only the user themself could
tell it apart from them actually speaking. Use case: videos that mix
on-camera segments with voiceover-only segments, with no audible seam
between the two.

## Context

- Chosen approach: **cloud API (ElevenLabs)**, not a local model — decided
  2026-08-03 because a genuinely indistinguishable clone realistically needs
  it; this machine is Intel/CPU-only with no GPU acceleration, so a local
  open-source model (Coqui XTTS-v2 etc.) would be both slower and more
  audibly synthetic. Local was declined in favor of quality.
- This is the user's own voice, cloned with their own consent for their own
  content — no third-party voice data involved. Keep it that way: don't feed
  in anyone else's voice without their explicit consent. ElevenLabs requires
  identity verification before a **Professional** clone can be used, which
  exists specifically to make cloning someone else's voice without consent
  harder — don't work around that.
- "Learn over time" maps directly onto ElevenLabs' **Professional Voice
  Cloning (PVC)** tier: add more samples whenever new clean recordings exist,
  then re-train. Instant Voice Cloning (IVC) also exists for a fast first
  result while there isn't much audio yet.

## Current state

**Scaffolded, not yet usable.** Code/CLI is written and works structurally,
but nothing can actually run until the user:
1. Creates an ElevenLabs account and gets an API key
   (https://elevenlabs.io/app/settings/api-keys) — needs a paid plan for
   real usage (there's a free tier, but it's limited).
2. Copies `.env.example` to `.env` and fills in `ELEVENLABS_API_KEY`.
3. Records/gathers voice samples: clean audio, no background noise or
   music, ideally varied sentences/emotions. Drops them into `samples/`.
   - For a fast first result: a few minutes is enough for `ivc-create`.
   - For the best/longest-term result: ElevenLabs recommends 30+ minutes
     of varied audio for **PVC**, plus completing their identity
     verification step in the dashboard before training.

Once those three things exist, the actual clone creation is one command
(see Environment → Setup below).

## Environment

**Requirements**: Python packages `elevenlabs` + `python-dotenv` (installed
2026-08-03, `pip3 install --user`); an ElevenLabs account + API key (not
installable by an agent — the user has to create this).

**Verify**:
```bash
python3.12 -c "import elevenlabs, dotenv" && echo "packages OK"
test -f /Users/apple/dev/work-with-ai/projects/ai-voiceover/.env && \
  grep -q "^ELEVENLABS_API_KEY=.\+" /Users/apple/dev/work-with-ai/projects/ai-voiceover/.env && \
  echo "API key configured" || echo "MISSING: .env with a real ELEVENLABS_API_KEY"
```

**Setup**:
```bash
pip3 install --user elevenlabs python-dotenv   # if the packages check fails
cd /Users/apple/dev/work-with-ai/projects/ai-voiceover
cp .env.example .env   # then fill in ELEVENLABS_API_KEY by hand
```

**Using it** (once samples exist and `.env` has a real API key):
```bash
cd /Users/apple/dev/work-with-ai/projects/ai-voiceover

# Fast first clone (few minutes of samples/ audio is enough):
python3.12 scripts/voice.py ivc-create --name "My Voice"

# OR the higher-fidelity, improves-over-time path:
python3.12 scripts/voice.py pvc-create --name "My Voice" --language en
# → then verify identity in the ElevenLabs dashboard for that voice_id
python3.12 scripts/voice.py pvc-add-samples --voice-id <id>
python3.12 scripts/voice.py pvc-train --voice-id <id>
# → whenever new samples are added later: pvc-add-samples again, then pvc-train again

# Generate a voiceover from a transcript:
python3.12 scripts/voice.py generate --text-file transcript.txt --out output/scene3.mp3
# (voice_id defaults to whatever ivc-create/pvc-create last saved to .env)
```

`samples/` and `output/` are gitignored — voice recordings and generated
audio never get committed, only the code/config does.

## Work Log

### 2026-08-03 — Scaffolded
- Decided cloud (ElevenLabs) over local, given CPU-only hardware and the
  "indistinguishable" bar.
- Installed `elevenlabs` + `python-dotenv` (pip, user site-packages).
- Inspected the actual installed SDK (v2.60.0) rather than assume its
  shape — API used: `client.voices.ivc.create`, `client.voices.pvc.create` /
  `.samples.create` / `.train`, `client.text_to_speech.convert`.
- Built `scripts/voice.py` (single CLI, subcommands: ivc-create, pvc-create,
  pvc-add-samples, pvc-train, generate).
- Not yet usable: needs the user's ElevenLabs account/API key and actual
  voice sample recordings — neither of which an agent can supply. That's
  the next step before this can produce a real voiceover.
