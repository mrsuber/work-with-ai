# SuberCraftex

**Category: Private/Personal**

## Purpose

A full-stack e-commerce platform (web + mobile) for SuberCraftex, covering
product management, order processing, supplier integration, delivery
tracking, and customer reviews — a production-oriented retail business
system, not just a storefront.

**Bigger picture** (see `MISSION.md` and
`family-social-site-pes-01`'s `MASTER-MISSION-DOCUMENT.md`): SuberCraftex
is envisioned as a vertically-integrated manufacturing ecosystem (crafts →
furniture → cars → spacecraft, per `CURRICULUM_MASTER_PLAN.md`), explicitly
governed by Islamic principles (no riba, zakat built into the profit model,
Shura-based decisions) — not just a normal e-commerce business. See
[Islamic Study & Practice](../islamic-study/PROJECT.md) for why that's not
incidental.

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
tooling for builds. For the curriculum's Fusion 360 design/CAM work (see
below): Autodesk Fusion (Personal/free edition works), `uv`/`uvx`, and the
`fusion360` MCP server. For 3D modeling/rendering work (see Blender MCP
below): Blender 4.5 LTS (the last release with an official Intel macOS
build — see that section for why), `uv`/`uvx`, and the `blender` MCP server.

**Verify**:
```bash
test -d ~/dev/SuberCraftex-ecommerceWeb/.git && echo "web cloned"
test -d ~/dev/SuberCraftex-ecommerceApp/.git && echo "app cloned"
claude mcp get fusion360   # should show "Status: ✔ Connected"
lsof -iTCP:9876 -sTCP:LISTEN -P -n   # should show an Autodesk process (add-in running inside Fusion)
claude mcp get blender     # should show "Status: ✔ Connected"
lsof -iTCP:9877 -sTCP:LISTEN -P -n   # should show a Blender process (addon socket server running inside Blender)
# If nothing's listening on 9877, Blender.app needs to actually be running (GUI, not just installed) —
# open it: `open -a /Applications/Blender.app`
```

**Setup**:
```bash
cd ~/dev/SuberCraftex-ecommerceWeb && npm install && cp .env.example .env   # fill in Stripe/Supabase values
cd ~/dev/SuberCraftex-ecommerceApp && npm install
```

### Fusion 360 MCP (design/CAM tooling)

For the CAD/CAM work in `CURRICULUM_MASTER_PLAN.md` (Fusion 360 design,
CAM/G-code generation). Set up 2026-08-03:

- **Official Autodesk MCP server is NOT available** — it's gated to paid
  Fusion subscriptions (Preferences → General → API has no "Fusion MCP
  Server" option at all on Fusion Personal/free, which is what's installed
  here). Confirmed by actually checking, not assumed.
- Used the community **`faust-machines/fusion360-mcp-server`** instead
  (MIT, 65 stars, actively maintained, 89 tools, tested with Claude Code) —
  vetted before installing: checked stars/forks/issues/license, read the
  actual add-in source (clean, localhost-only TCP, no obfuscation).
  Cloned to `~/dev/fusion360-mcp-server`.
- **Known bug worked around**: the package declares `mcp>=1.0` with no
  upper bound; the `mcp` Python SDK's 2.0.0 release broke its API
  (`Server.list_tools` no longer exists), and `uvx` resolves latest by
  default. Fixed by pinning: registered as
  `uvx --with "mcp<2.0" fusion360-mcp-server --mode socket` (1.26.0 is what
  the project's own `uv.lock` was built/tested against). If this package
  releases a fixed version later, the `--with "mcp<2.0"` override can
  probably be dropped — check first before assuming still needed.
- Architecture: Fusion360MCP **add-in** (copied to
  `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/Fusion360MCP`)
  runs inside Fusion, listens on `localhost:9876`; the MCP server itself is
  a separate stdio process Claude Code spawns via `uvx`. **Both pieces
  needed**: Fusion must be running with the add-in started (Shift+S →
  Add-Ins → Fusion360MCP → Run, or set "Run on Startup") *and* registered
  with `claude mcp add`.
- Registered at **user scope** (`claude mcp get fusion360` → Connected) —
  available in any project, not just this one.
- **Not yet verified with a real tool call** — added mid-session, and (same
  as the `figma` plugin) new MCP tools don't show up in an already-running
  Claude Code session. First session after a restart: call `ping` (should
  return `{"pong": true}`) with Fusion running and the add-in started,
  before relying on it for real design work.

### Blender MCP (3D modeling/rendering tooling)

For general 3D work in the curriculum/ecosystem (product visualization,
scene/asset creation) — same pattern as Fusion 360 above, different tool.
Set up 2026-08-04:

- **Blender 5.x does NOT run on this machine.** This is a genuine Intel Mac
  (MacBookPro16,1, i9-9880H — confirmed via `sysctl`, not Rosetta on Apple
  Silicon). Blender dropped Intel macOS builds as of 5.0; **4.5 LTS is the
  last release with an official Intel build** (supported with patches into
  ~2027). Installed **4.5.12** (the latest 4.5.x patch as of setup) from
  `https://download.blender.org/release/Blender4.5/blender-4.5.12-macos-x64.dmg`.
  Before reaching for "latest," check `uname -m`/`sysctl machdep.cpu.brand_string`
  isn't reporting a Rosetta-translated x86_64 on what's actually Apple
  Silicon — the two look identical from `uname -m` alone.
- The old Blender 3.6.4 (installed 2023) was moved to Trash, not deleted
  outright, before installing 4.5.12 in its place.
- Used the official **`ahujasid/blender-mcp`** project (cloned to
  `~/dev/blender-mcp`) — addon (`addon.py`) copied into the *version-specific*
  addon folder, `~/Library/Application Support/Blender/4.5/scripts/addons/addon.py`
  (Blender addon paths are per-version; reinstalling/upgrading Blender means
  re-copying the addon into the new version's folder).
- **Port conflict avoided deliberately**: the addon's default port is 9876,
  which the Fusion 360 add-in (above) already holds. Reconfigured to
  **9877** via the addon's `scene.blendermcp_port` property, and confirmed
  with a full `lsof -iTCP -sTCP:LISTEN` sweep that 9877 isn't used by
  anything else on this machine (Fusion=9876, DaVinci Resolve=49152, Figma
  holds no fixed local port). Registered the MCP server at user scope with
  `BLENDER_PORT=9877` in its env so the two 3D tools' MCP servers can run
  side by side without collision.
- **Known startup race**: the addon's `register()` reads
  `bpy.context.scene.blendermcp_port` to auto-start the server, but when
  Blender loads an addon that was already enabled at previous shutdown,
  `bpy.context.scene` isn't reliably available yet at that exact moment —
  it can silently fall back to the hardcoded default (9876) and fail to
  bind (port already taken by Fusion), leaving the server not running with
  no obvious error in the UI. Worked around by driving setup through a
  `--python <script>` launch (not `--background` — the addon explicitly
  refuses to start its server in background mode) that explicitly calls
  `bpy.ops.blendermcp.stop_server()`, sets `scene.blendermcp_port = 9877`,
  calls `bpy.ops.blendermcp.start_server()`, then
  `bpy.ops.wm.save_userpref()` + `bpy.ops.wm.save_homefile()` so the
  correct port is baked into the default startup file for next time.
- Registered at **user scope** (`claude mcp get blender` → Connected).
- **Verified with real tool calls, both read and write**:
  `mcp__blender__get_scene_info` returned the live default scene
  (Cube/Light/Camera); `mcp__blender__execute_blender_code` then generated
  actual geometry (a beveled torus with a material, 768 verts/edges/faces)
  and `mcp__blender__get_object_info` + `mcp__blender__get_viewport_screenshot`
  confirmed it existed and rendered correctly, before deleting it again to
  leave the scene clean. Not just "Connected" in config — genuinely
  generates models end to end, as of 2026-08-04.

## Work Log

### 2026-08-03 — Indexed
- Cloned both repos fresh into `~/dev/`.
- Discovered and flagged three other local `subercraftex` folders under
  different remotes/accounts with real uncommitted work — left untouched,
  needs the user's input on what they actually are before any action.

### 2026-08-03 — Fusion 360 MCP set up
- Confirmed official Autodesk MCP server unavailable on Fusion Personal
  (free) — no such preference exists in Preferences → General → API.
- Installed community `faust-machines/fusion360-mcp-server` instead after
  vetting it. Hit and fixed a real dependency bug (unpinned `mcp>=1.0`
  breaking against `mcp` 2.0.0) — see Environment section above for the
  fix. Registered at user scope, `claude mcp get fusion360` shows
  Connected. Not yet verified with an actual tool call — pending a Claude
  Code restart (tools don't load into an already-running session).

### 2026-08-04 — Blender MCP set up (Blender reinstalled, 3.6.4 → 4.5.12 LTS)
- Picked up a half-finished setup from a prior, undocumented session (found
  via `.claude/settings.local.json` permission grants matching this exact
  investigation, and `~/dev/blender-mcp` already cloned) — this entry is
  what makes it show up next time instead of getting re-discovered cold.
- Investigated "download the recent Blender" and found latest-overall
  (5.2 LTS) doesn't run on this Intel Mac at all; installed **4.5.12 LTS**
  instead, the actual last Intel-compatible release. Old 3.6.4 moved to
  Trash (recoverable, not deleted outright).
- Wired the addon to port **9877** specifically to avoid the Fusion 360
  add-in's 9876, verified against a full port scan (see Environment section
  above for the full detail on why and how — including a startup-race
  gotcha in the addon itself worth reading before touching this again).
- Verified end-to-end with a live `mcp__blender__get_scene_info` call
  against the running Blender instance — genuinely connected, not just
  "Connected" in `claude mcp get`.
- Not yet used for actual curriculum/product work — this session was setup
  and verification only.
