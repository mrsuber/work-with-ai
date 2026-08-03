# SuberCraftex

**Category: Private/Personal**

## Purpose

A full-stack e-commerce platform (web + mobile) for SuberCraftex, covering
product management, order processing, supplier integration, delivery
tracking, and customer reviews — a production-oriented retail business
system, not just a storefront.

## Context

Two repos, one product:

- **Web** — `git@github.com:mrsuber/SuberCraftex-ecommerceWeb.git`, cloned
  at `~/dev/SuberCraftex-ecommerceWeb`. Next.js 15 + TypeScript. Multi-role
  auth (Admin/Customer/Driver), Stripe checkout + webhooks, real-time order
  tracking with driver assignment, review system, inventory management with
  audit logs, supplier purchase-order workflow, analytics dashboard. Prisma
  + Supabase.
- **App** — `git@github.com:mrsuber/SuberCraftex-ecommerceApp.git`, cloned
  at `~/dev/SuberCraftex-ecommerceApp`. Expo/React Native (expo-router,
  TanStack Query, EAS for builds).

**Important — unrelated local folders with the same name**: there are three
*other* local `subercraftex`-named directories on this machine that are
**not** these repos and were left untouched:
- `~/dev/subercraftex` → remote `projectExpansionComplex/subercraftex`, 13
  uncommitted changed files
- `~/dev/myWebProjects/subercraftex` → remote `mrsuberwork/subercraftex`
  (different GitHub account, `dev` branch), 53 uncommitted changed files
- `~/dev/apps/subercraftex` → not a git repo at all

Whether those are legacy/abandoned copies, a different account's parallel
work, or something that should be reconciled with the two repos above is
unresolved — flagged to the user 2026-08-03, not yet followed up on. Don't
assume they're irrelevant; ask before treating them as safe to ignore or
delete.

## Current state

Both repos have substantial real content already (not fresh scaffolds) —
this index entry was created by linking existing work, not starting from
scratch. Haven't yet dug into current feature status/what's actively being
worked on beyond what the README/package.json show.

## Environment

**Requirements**: Node.js + npm for both. Web additionally needs Stripe +
Supabase credentials (see `.env.example` in the web repo). App needs Expo/EAS
tooling for builds.

**Verify**:
```bash
test -d ~/dev/SuberCraftex-ecommerceWeb/.git && echo "web cloned"
test -d ~/dev/SuberCraftex-ecommerceApp/.git && echo "app cloned"
```

**Setup**:
```bash
cd ~/dev/SuberCraftex-ecommerceWeb && npm install && cp .env.example .env   # fill in Stripe/Supabase values
cd ~/dev/SuberCraftex-ecommerceApp && npm install
```

## Work Log

### 2026-08-03 — Indexed
- Cloned both repos fresh into `~/dev/`.
- Discovered and flagged three other local `subercraftex` folders under
  different remotes/accounts with real uncommitted work — left untouched,
  needs the user's input on what they actually are before any action.
