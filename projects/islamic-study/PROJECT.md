# Islamic Study & Practice

**Category: Private/Personal — spiritual/intellectual, not software.**

## Purpose

Not just Quran memorization — learning Islam comprehensively: theology,
fiqh (jurisprudence), governance/business-ethics principles, history. This
is the first and ongoing front of the four-part mission (spiritual,
financial, physical, mental) in `MISSION.md`, and it is directly load-
bearing for SuberCraftex/SuberFood, not separate from them.

## Why this connects directly to SuberCraftex/SuberFood

Per `family-social-site-pes-01`'s `MASTER-MISSION-DOCUMENT.md` (§"Islamic
Governance Framework", ~line 935) — after explicit comparative-religion
study, Islam was chosen as **the actual governing framework for the whole
SuberCraftex/SuberFood ecosystem**, not a personal add-on:

- **Business ethics**: no riba (interest) — profit-sharing/Musharakah
  (partnership) and Murabaha (cost-plus, no interest) instead of
  interest-based financing; zakat (2.5% annually) built into the business
  model; full product traceability and honest pricing as religious
  obligation, not just good practice.
- **Halal standards**: mandatory for all SuberFood production.
- **Governance model**: Shura (consultation) for major decisions, Adl
  (justice/fairness) in treatment regardless of rank, Amanah
  (trustworthiness/stewardship) for anyone in a leadership role.
- **Employee relations**: prayer times accommodated in the work schedule,
  fair/timely wages, Ramadan and Hajj accommodations.
- **Long-term vision**: the document explicitly extends this to *space
  governance* — how the eventual spacecraft-building arm of SuberCraftex
  (see `CURRICULUM_MASTER_PLAN.md`) would ethically govern settlements,
  treat newly discovered environments, etc.

The document is explicit: *"This is NOT a religious decoration or
marketing. Islam is the ACTUAL operating system"* for decisions, money,
product-building, and organizational growth. So studying Islam
comprehensively isn't separate personal development running alongside the
business builds — it's what makes it possible to actually run SuberCraftex/
SuberFood the way they're designed to be run.

## Current state

**As of 2026-08-03**: known ongoing practice is nightly Quran memorization,
roughly 4am until Subhi (Fajr) prayer, described by the user as a struggle.
The fuller scope (fiqh, governance principles, etc.) is confirmed by the
mission document above, but no specifics on current study beyond the
nightly memorization have been shared yet — don't assume progress or
invent specifics; log what's actually shared as it comes up.

## Work Log

### 2026-08-03 — Corrected scope
- Originally scoped this narrowly as "Quran memorization" — corrected by
  the user: it's learning all of Islam, and the reason why is documented
  in the SuberCraftex/family-social-site mission docs (the Islamic
  Governance Framework in `MASTER-MISSION-DOCUMENT.md`), not just personal
  spiritual practice separate from the business builds.

### 2026-08-04 — First video-production pass: intro clip about the memorization struggle
- Source footage: `~/Downloads/phone raw photage/july/19/20260719_051923.mp4`,
  18:23, recorded 2026-07-19 at 05:37am — squarely in the nightly-memorization/
  post-Fajr window described above. Content, per the user directly: an
  introductory video about the daily struggle of memorizing the Arabic Quran
  — this is the first piece of the honest, unpolished documentation
  `MISSION.md` calls for (struggles and frustrations, not just highlights).
- Edited in DaVinci Resolve (project "Introduction to islam", timeline
  `Intro - Quran Memorization Struggle`) via the `davinci-resolve-mcp`
  project's MCP tools. Full technical detail (bugs hit, workarounds, exact
  steps) is logged in that project's own journal — see
  `davinci-resolve-mcp/PROJECT.md` → `RESOLVE_MCP_JOURNAL.md`,
  2026-08-04 entry — this entry only covers what's specific to *this piece
  of content*.
- Work done: corrected an overexposed/blown-highlight color grade, measured
  and fixed genuinely very quiet audio (~-34 LUFS raw phone recording,
  corrected to -14 LUFS/-1.5dBTP), confirmed almost no dead air to trim
  (continuous narration, not a stop-start recording style), transcript/
  captions in progress.
- Generated assets (corrected audio, transcript) permanently stored at
  `~/Movies/islamic-study-video-production/` — separate from the raw source
  in Downloads and from this git repo (media doesn't belong in git history).
- Not yet done: captions/subtitles not yet added to the timeline itself
  (transcript generation was in progress at end of session), no cut/trim
  pass on framing or background clutter, not yet exported/published.

### 2026-08-06 — First video published: final render, thumbnail, YouTube upload
Continuation of the 2026-08-04 entry above — same clip, taken from graded
edit through to a real (unlisted) YouTube upload. This is the actual first
publish of the mission's documentation effort described in `MISSION.md`.

- **Transcript/captions: skipped for this video, on purpose.** Local Whisper
  (`tiny` model) hung for 78+ minutes on this Intel Mac with no GPU — killed
  it. Tried faster-whisper on the Fayshaa smart-home server
  (`192.168.1.127`, see that project's own setup doc) as a second attempt:
  installed cleanly, but the model-weight download itself stalled
  (~2KB/s to Hugging Face) — same network-throttling pattern as the Mac, just
  a different host, so it's a network problem, not a hardware one. Also
  confirmed directly via `ollama list`/`ollama ps` on that server that **none
  of the 13 installed Ollama models can transcribe audio at all** — they're
  text-only LLMs; that's a hard capability limit, unrelated to the network
  issue. User decided: publish without captions now, revisit once a real
  transcription path exists (their own OpenAI-API-key offer, or patiently
  retrying the faster-whisper model download). The reusable pieces are still
  in place for next time: `faster-whisper` installed in
  `~/whisper-agent/venv` on the Fayshaa server, working script at
  `~/whisper-agent/transcribe_agent.py` (SRT/VTT/TXT output), passwordless
  SSH configured from this Mac. Whoever picks this up next just needs the
  model weights to actually finish downloading.
- **Final render**: full timeline (graded + corrected audio) exported via
  DaVinci Resolve's render queue to
  `~/Movies/islamic-study-video-production/exports/Intro-Quran-Memorization-Struggle_v1.mp4`
  (H.264, ~5.7GB, ~7 min render time). Exporting to a non-temp directory
  needs `require_temp_target: false` on `render.prepare_render_job` — logged
  in the Resolve MCP journal too.
- **Thumbnail**: built in Figma from a color-graded frame — uploaded the
  frame as an image fill, added a dark gradient scrim + bold white title
  text ("MY QURAN MEMORIZATION STRUGGLE") for legibility over the busy
  background, exported at 1280x720. Saved to
  `~/Movies/islamic-study-video-production/thumbnail/`. **Figma account
  note**: this account is Starter tier / View seat — capped at **6 MCP tool
  calls per month** (only `whoami`, `generate_figma_design`, and
  `add_code_connect_map` are exempt). This one thumbnail used 5 of the 6 —
  budget carefully next time, or upgrade the seat if thumbnails become a
  regular per-video task.
- **YouTube upload**: channel "SUBER-Craftex" — this was its first-ever
  video. First attempt failed after a full 5.7GB upload: **"Processing
  abandoned — video is too long"** — YouTube caps unverified channels at 15
  minutes; this video is 18:23. User verified the channel (Settings → Channel
  → Feature eligibility → phone verification unlocks "Videos over 15
  minutes"), confirmed Enabled, then re-uploaded. Title "My Quran
  Memorization Struggle", honest description written to match `MISSION.md`'s
  tone (struggles included, not just highlights), custom thumbnail attached,
  visibility set to **Unlisted** (deliberate choice for a first upload with
  no captions and unaddressed background/framing clutter — reviewable via
  link, not publicly searchable yet). User confirmed the upload itself
  completed; the metadata/visibility steps in the Studio dialog were still
  being driven via browser automation when the session ended — **worth a
  quick manual check that Unlisted actually saved** before treating this as
  fully done.
- Not yet done: captions still missing, no background/framing cleanup, no
  verification that the final visibility setting saved correctly (see above).
