# Suber Foods (SuberFood)

**Category: Private/Personal**

## Purpose

A vertical-integration farm-to-table platform: manage the entire food supply
chain from farm to consumer — farming operations (crops, livestock,
aquaculture, poultry), processing, logistics/warehousing, restaurants, and
retail (B2B + D2C), with full traceability across the chain.

## Context

- **Repo**: `git@github.com:mrsuber/SuberFood.git`, cloned at
  `~/dev/SuberFood`. Real, actively developed — not the placeholder this
  entry originally was (see Work Log).
- **Architecture**: Turborepo + npm workspaces monorepo. `apps/` (frontend
  apps: landing-page, admin-dashboard, farm-management, restaurant-pos,
  retail-platform, mobile-app) + `services/` (backend microservices: farm,
  livestock, aquaculture, processing, logistics, warehouse, quality,
  restaurant, retail, order, customer, partner, and more).
- Currently only `apps/landing-page` has real work in it — the rest of the
  monorepo structure exists but isn't built out yet.
- Prisma (`@prisma/client`) for data; currency is XAF (Central African
  Franc) — this is a Cameroon-market business, consistent with the user's
  other Cameroon-based projects.

## Current state

Active development, focused on the landing page's **Distribution →
Restaurants** module as of the most recent work (per
`DEVELOPMENT-PROGRESS.md`, dated May 2026): premium UI component library,
restaurant section with nutritional info display, recipe pages, seed
scripts. Most recent commits are small fixes (currency display, Prisma
relation/seed script bugs).

## Environment

**Requirements**: Node.js, npm (Turborepo monorepo — installs are
workspace-wide from repo root); Prisma (needs a configured database for
anything beyond static pages — check `.env.example` / `.env.production.template`
for what's needed, likely Postgres).

**Verify**:
```bash
test -d ~/dev/SuberFood/.git && echo "cloned"
cd ~/dev/SuberFood && node -e "require('./package.json')" && echo "package.json OK"
```

**Setup**:
```bash
cd ~/dev/SuberFood
npm install
cp .env.example .env   # fill in real values (DB connection, etc.) before running anything that touches data
```

## Work Log

### 2026-08-03 — Linked to real repo
- Originally seeded 2026-08-03 as a placeholder from just a name + one-line
  description, before the actual repo existed in this index.
- Repo `mrsuber/SuberFood` cloned to `~/dev/SuberFood` (already had
  substantial real content — not a fresh project). Purpose/Context/Current
  state above rewritten from what's actually in the repo (README, recent
  git log, DEVELOPMENT-PROGRESS.md) rather than the earlier placeholder
  guess.
