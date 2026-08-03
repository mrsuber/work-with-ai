# Family Social Site (pes-01)

**Category: Private/Personal**

## Purpose

Started as a family/social networking site, but has grown well beyond that
name — the codebase now includes a "Mission Control" operations system
(department/personnel/asset/financial dashboards, calendar, diary), a
restaurant management module (menu, inventory, POS, orders), an Islamic
LMS (courses, lessons, assignments), and global asset/landmark tracking —
alongside the original family/social features. Treat the repo name as
historical, not descriptive of current scope.

## Context

- **Repo**: `git@github.com:mrsuber/family-social-site-pes-01.git`,
  **already cloned** at `~/dev/myWebProjects/family-social-site-pes-01`
  (not under `~/dev/` directly — that's just where the user already had it;
  left in place rather than re-cloned).
  - Also has a `heroku` remote (`git.heroku.com/msb-geneasocial.git`) —
    deployed there.
- **Stack**: Node/Express backend (Sequelize/Postgres primarily, some
  Mongoose/MongoDB too — mixed, not fully reconciled), React frontend
  (Material-UI, ReactFlow for the node-graph "Mission Control" views,
  Google Maps, Socket.io for real-time).
- Extensive markdown docs at repo root (`MASTER-MISSION-DOCUMENT.md`,
  `PROJECT_COMPREHENSIVE_ANALYSIS.md`, `GLOBAL_ASSETS_SYSTEM.md`,
  `RESTAURANT-MISSION-CONTROL-INTEGRATION.md`, etc.) — these are likely the
  real source of truth for current scope/architecture; worth reading before
  doing serious work here rather than relying on this summary.

## Current state

Actively developed — pulled 18 commits (257 files changed) on 2026-08-03
that hadn't been fetched yet. Recent work spans mission-control dashboards,
restaurant management, Islamic course LMS, and global asset/landmark
tracking. Deployment docs (`DEPLOYMENT_INSTRUCTIONS_MAY_2026.md`,
`DEPLOYMENT_SUCCESS.md`) suggest this has real deployed usage, not just dev.

## Environment

**Requirements**: Node.js + npm (both root/backend and `client/`); a
Postgres database (Sequelize) and possibly MongoDB (Mongoose) — check
`config/db.js` and `.env.production` for what's actually configured; Heroku
CLI if deploying.

**Verify**:
```bash
cd ~/dev/myWebProjects/family-social-site-pes-01
git status --short --branch   # should be clean, up to date with origin/master
node -e "require('./package.json')" && echo "backend package.json OK"
node -e "require('./client/package.json')" && echo "client package.json OK"
```

**Setup**:
```bash
cd ~/dev/myWebProjects/family-social-site-pes-01
npm install
cd client && npm install
# DB config: see config/db.js and .env.production for what needs filling in
```

## Work Log

### 2026-08-03 — Indexed, pulled latest
- Confirmed already cloned at `~/dev/myWebProjects/family-social-site-pes-01`,
  matching `origin` exactly; working tree was clean.
- Fetched + fast-forward pulled: 18 commits behind, 257 files changed,
  65395 insertions — no conflicts.
- Purpose/Context above written from actual file structure (this repo has
  expanded far past "family social site" into a broader personal/business
  operations system) rather than assumed from the repo name.
