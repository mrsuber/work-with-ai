# DaVinci Resolve MCP

## Purpose

Give Claude Code live control of DaVinci Resolve (free edition) via an MCP
server, so editing/project work in Resolve can be driven through natural
language instead of manual clicking.

## Context

This project lives in **its own repo**, not inside `work-with-ai` — it's
substantial enough (a full MCP server, an in-app bridge, its own upstream
project) to warrant that. This file is a thin pointer, not a duplicate
journal.

- **Repo**: `git@github.com:mrsuber/davinci-resolve-mcp.git` (personal fork,
  full history + `upstream` remote pointing at `samuelgursky/davinci-resolve-mcp`)
- **Clone location convention**: `~/dev/davinci-resolve-mcp`
- **Full journal**: `RESOLVE_MCP_JOURNAL.md` inside that repo — read that
  file for the actual Work Log, gotchas, and detailed setup. This file just
  gets it onto the index and gives a fast Environment check.

## Current state

Fully working as of 2026-08-03: MCP server registered in Claude Code (user
scope), in-app bridge connects to the running (free-edition) Resolve
install, verified against a live project.

First real editing session (not just a connection test) done 2026-08-04 —
color + audio correction pass on a real clip. Surfaced real gotchas (macOS
file-access restrictions on Downloads, an MCP color-grading bug, render
workflow quirks) — all logged in `RESOLVE_MCP_JOURNAL.md`'s 2026-08-04 entry
in the project's own repo. Read that entry before the next editing session;
it'll save re-discovering the same traps.

## Environment

**Requirements** — the repo cloned locally; a Python venv inside it; a
python.org **framework** Python (separate from the venv) for the in-app
bridge; DaVinci Resolve running with a project open and `resolve_bridge`
started from Workspace ▸ Scripts.

**Verify**:
```bash
test -d ~/dev/davinci-resolve-mcp || echo "MISSING: clone the repo (see below)"
claude mcp get davinci-resolve   # should show "Status: ✔ Connected"
lsof -iTCP:49632 -sTCP:LISTEN    # should show a `fuscript` process (bridge running)
```
If the MCP entry is missing or bridge isn't listening, DaVinci Resolve
either isn't running, doesn't have a project open, or `resolve_bridge`
hasn't been (re-)started from Workspace ▸ Scripts since Resolve last
launched — that last one needs doing every time Resolve restarts, it does
not persist.

**Setup** (fresh machine, first time):
```bash
mkdir -p ~/dev && cd ~/dev
git clone git@github.com:mrsuber/davinci-resolve-mcp.git
cd davinci-resolve-mcp
python3 install.py            # creates venv, installs MCP SDK
# then follow RESOLVE_MCP_JOURNAL.md for: framework Python install,
# claude mcp add (user scope), and the in-app bridge install/start —
# those are one-time-per-machine and have enough nuance (free vs Studio
# edition, framework-Python detection) that they're kept in the full
# journal rather than duplicated here.
```

## Work Log

See `RESOLVE_MCP_JOURNAL.md` in the project's own repo — that's where this
project's actual Work Log lives, kept in one place rather than split across
two repos.
