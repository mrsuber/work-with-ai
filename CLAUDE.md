# Work With AI — Operating Instructions

This repo is the persistent index for every project built with Claude Code
here. It exists so that referencing this repo — opening a session in this
directory, or just naming a project that lives in it — is enough to pick up
exactly where things left off, instead of re-explaining context every time.

**Read this file, then `MISSION.md`, then `INDEX.md`, before doing anything
else in this repo.** `MISSION.md` is the "who/what/why" behind the
Private/Personal projects — read it before making any call on priority or
sequencing.

`INDEX.md` splits projects into **Private/Personal** and **Client** — keep
that distinction when adding new ones. It matters for things like tone,
what's okay to reference across projects, and billing/scope boundaries on
client work; don't blur the two without the user saying so.

## The first move, every time

This applies whether this is the machine that's always run this project, or
a brand new machine that just cloned this repo for the first time — the
steps are the same either way, which is the point.

1. Open `INDEX.md`. Find the project being discussed (or figure out it's
   new).
2. **New project** → create `projects/<slug>/PROJECT.md` from
   `projects/_TEMPLATE.md`, add a row to `INDEX.md`, and start at **Think**
   below. Its Environment section starts empty — there's nothing to verify
   yet, and setup requirements get written down as they're discovered during
   Think/Plan, not guessed upfront.
3. **Continuing project** → read `projects/<slug>/PROJECT.md` in full,
   especially its Work Log, before responding. Don't ask the user to
   re-explain what's already written down there.
4. **Environment check (continuing projects only, every session)** — before
   doing any real work, run that project's Environment → Verify steps.
   - All good → say nothing about it, just proceed.
   - Something missing/broken → run the Setup steps to fix it. For anything
     system-wide, destructive, or requiring credentials, confirm with the
     user first rather than just doing it (standard practice, not special
     to this repo) — but routine stuff (installing a project's own declared
     dependencies, creating a venv) doesn't need a confirmation each time.
   - Setup steps are missing, wrong, or incomplete for what's actually on
     this machine → fix them, and update the Environment section in
     `PROJECT.md` so the next machine doesn't hit the same gap. This is the
     mechanism that makes a fresh clone on a new computer actually work —
     if this step gets skipped, that guarantee quietly breaks.
   - Only once the environment is actually verified working, move on to
     what the user actually asked for.

Never skip straight to building without doing step 1 (and step 4, for a
continuing project).

## The crew

This is one agent, not five apps — the tools/skills below already give one
Claude Code session everything the "Chat / Projects / Cowork / Code / Chrome"
stack gives a team, so there's no separate app-switching. Adapted (and
extended past the original 5) from the workflow in
`projects/_reference/how-to-use-claude-video.md`:

1. **Remember** — load context first (`INDEX.md` + the project's
   `PROJECT.md`), then run its Environment check (see "The first move"
   above). This is the step the video's "Projects" tool covers; here it's
   reading the file *and* confirming the environment it describes is
   actually true on this machine before trusting it.
2. **Think** — brainstorm/scope a fuzzy idea into something concrete before
   building anything. Use the `brainstorming` skill (superpowers plugin) for
   anything non-trivial. Apply **PRIME** (below) to figure out what's
   actually being asked.
3. **Research** — ground the thinking in real data: web search/fetch,
   existing files, prior Work Log entries. Verify anything load-bearing
   rather than assuming — same rule the video gives for AI research: ask
   "is this verified?"
4. **Plan** — once scope is real, write the plan down (`writing-plans`
   skill) rather than holding it only in conversation, especially for
   anything that will span more than one session.
5. **Build** — execute the plan. For code: TDD (`test-driven-development`),
   `systematic-debugging` when stuck, `subagent-driven-development` /
   `dispatching-parallel-agents` for anything large enough to parallelize.
   For non-code deliverables, build the actual artifact, not a description
   of one.
6. **Verify** — `verification-before-completion` before calling anything
   done. For code changes, `requesting-code-review` /
   `receiving-code-review`.
7. **Browse** — when the task needs live interaction with a website or app
   rather than just reading it, use the `claude-in-chrome` skill. Distinct
   from Research: Research reads, Browse acts.
8. **Document** — before ending a session (or a major chunk of work),
   append to that project's Work Log in its `PROJECT.md`: what was decided,
   what was built, what's next. Update its status/date in `INDEX.md`. This
   is what makes step 2 ("the first move") actually work next time — a
   session that skips this step breaks continuity for the next one.

Not every project needs all eight every session — a quick fix might only
need Remember → Build → Document. Use judgment about how much ceremony a
given ask actually needs; the point is continuity, not process for its own
sake.

## PRIME — how to scope an ambiguous ask

From the same source video. Use this to turn a vague request into a clear
one, especially during **Think**:

- **P**urpose — what is this actually for? What outcome does the user need?
- **R**esearch — what grounding does this need (files, prior work, web,
  verified facts) before acting on it?
- **I**nterview — when the ask is underspecified, ask clarifying questions
  rather than guessing — don't silently assume.
- **M**echanics — what should the output look like (format, length, where it
  lives)?
- **E**xamples — is there a reference, prior project, or style to match?

## Project lifecycle & structure

```
work-with-ai/
  CLAUDE.md              — this file
  INDEX.md               — one row per project: name, status, one-line description, path
  projects/
    _TEMPLATE.md          — copy this to start a new project
    <project-slug>/
      PROJECT.md          — Purpose/Context/Environment/Work Log
      ...                 — actual project files, code, docs, whatever it needs
```

Keep each project's own working files inside its `projects/<slug>/` folder.
`PROJECT.md` is the journal — read at the start of a session, appended to at
the end, not a one-time README. Its **Environment** section (Requirements /
Verify / Setup) is what step 4 of "The first move" runs — this is what lets
a brand new machine clone this repo, pick a project, and actually get to
working state without the human re-explaining setup from scratch.

A project doesn't have to live inside this repo — some are big enough to
warrant their own repo (e.g. `davinci-resolve-mcp`, which has its own
`RESOLVE_MCP_JOURNAL.md` using this same Purpose/Environment/Work Log
shape). Either way it still gets a row in `INDEX.md` and a
`projects/<slug>/PROJECT.md` — for an external repo, that file is a thin
pointer (where the repo is, how to clone it) rather than the full journal,
so there's still exactly one place to look to find out "what am I working
on and is it set up."

## Scope boundary

Only work within repos that are explicitly given and tracked in `INDEX.md`
— the ones actually cloned locally. Don't explore, read, or touch other
directories or repositories on this machine on your own initiative, even
ones that look related by name. (Full rationale in `MISSION.md` — this
came up concretely with several unrelated local `subercraftex`-named
folders under different remotes/accounts; they were flagged to the user,
not poked at further.)

## Related setup already in place

- **`superpowers`** Claude Code plugin (user scope, installed 2026-08-03) —
  the skills referenced above (brainstorming, writing-plans,
  test-driven-development, etc.) come from it and are available in every
  session automatically.
- **`figma`** Claude Code plugin (user scope, installed 2026-08-03) —
  official Figma MCP server + skills (`figma-generate-design`,
  `figma-create-new-file`, `figma-generate-library`, etc.), for making
  YouTube cover/thumbnail designs. Installed via
  `claude plugin install figma@claude-plugins-official`; OAuth login done
  (`claude mcp get "plugin:figma:figma"` → Connected). **Not yet verified
  with a real tool call** — the plugin was installed mid-session, and
  Figma's own setup guide says a Claude Code restart is needed before its
  tools actually show up. First session after a restart should do an actual
  test (e.g. create a small sample file) before relying on it for real
  thumbnail work.
- Claude's own memory system also holds a pointer to this repo, so it's
  recognized even from a session that didn't start in this directory —
  naming a project here should be enough.
