# Fayshaa

**Category: Client**

## Purpose

Client work for Fayshaa — a web app (live) plus a companion mobile app
(not started, design phase).

## Context

- **Web** — `git@github.com:mrsuber/FayshaaWeb.git`, cloned at
  `~/dev/FayshaaWeb`. React frontend + Node/Express backend, Firebase (push
  notifications + auth), PostgreSQL, i18next (multi-language), and
  `pannellum`/`pannellum-react` (360° panorama viewer) — likely a
  property/venue/tour-style site given the panorama viewer.
- **App** — no repo yet. Per the user: **will live in the same repo as
  Web** (`FayshaaWeb`) once work starts, not a separate one. Currently in
  **design phase only** — this is exactly the use case the Figma MCP setup
  (2026-08-03) was for.
- **Existing brand assets**: `~/dev/FayshaaWeb/docs/branding/` already has
  a full brand guidelines PDF (`Brand_Guidelines_faysha(3).pdf`) plus prior
  marketing collateral (flyers, social profile images, a YouTube cover, Ad
  creatives). **Use these as the source of truth for colors/fonts/logo**
  when doing any Figma design work for this client — don't improvise a
  visual identity that conflicts with what's already established.

## Current state

Web app has real, deployed-oriented content (Firebase setup checklists,
DNS/SSL/domain config docs, server setup docs — this is running
infrastructure, not a prototype). App is unstarted — next real step for it
is a Figma design session, not code.

## Environment

**Requirements** (Web): Node.js + npm for both `frontend/` and `backend/`;
Firebase project + service account credentials (`.env`, not in git); a
PostgreSQL database.

**Verify**:
```bash
test -d ~/dev/FayshaaWeb/.git && echo "cloned"
cd ~/dev/FayshaaWeb && node -e "require('./frontend/package.json')" && echo "frontend OK"
node -e "require('./backend/package.json')" && echo "backend OK"
```

**Setup**:
```bash
cd ~/dev/FayshaaWeb/frontend && npm install
cd ~/dev/FayshaaWeb/backend && npm install
# Firebase service account + .env files are gitignored -- get these from the client/user directly, not derivable from the repo
```

**App (design phase)**: no code environment yet. Needs: Figma MCP plugin
connected (see root `CLAUDE.md` → "Related setup already in place" — status
as of 2026-08-03 was installed + authenticated but **not yet verified with
a real tool call**, pending a Claude Code restart). Once verified, use the
brand assets above as the starting reference.

## Work Log

### 2026-08-03 — Indexed
- Cloned `FayshaaWeb`. Confirmed `FayshaaApp` has no separate repo — it
  will live inside `FayshaaWeb` once design work turns into code.
- Found existing brand guidelines + prior marketing collateral in
  `docs/branding/` — noted as the reference to use for the app's design
  rather than starting from a blank slate.
