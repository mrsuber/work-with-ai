# Work With AI — Operating Instructions

This repo is the persistent index for every project built with Claude Code
here. It exists so that referencing this repo — opening a session in this
directory, or just naming a project that lives in it — is enough to pick up
exactly where things left off, instead of re-explaining context every time.

**Read this file, then `INDEX.md`, before doing anything else in this repo.**

## The first move, every time

1. Open `INDEX.md`. Find the project being discussed (or figure out it's new).
2. **New project** → create `projects/<slug>/PROJECT.md` from
   `projects/_TEMPLATE.md`, add a row to `INDEX.md`, and start at **Think**
   below.
3. **Continuing project** → read `projects/<slug>/PROJECT.md` in full,
   especially its Work Log, before responding. Don't ask the user to
   re-explain what's already written down there.

Never skip straight to building without doing step 1.

## The crew

This is one agent, not five apps — the tools/skills below already give one
Claude Code session everything the "Chat / Projects / Cowork / Code / Chrome"
stack gives a team, so there's no separate app-switching. Adapted (and
extended past the original 5) from the workflow in
`projects/_reference/how-to-use-claude-video.md`:

1. **Remember** — load context first (`INDEX.md` + the project's
   `PROJECT.md`). This is the step the video's "Projects" tool covers; here
   it's just reading the file before talking.
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
      PROJECT.md          — that project's Purpose/Context/Work Log
      ...                 — actual project files, code, docs, whatever it needs
```

Keep each project's own working files inside its `projects/<slug>/` folder.
`PROJECT.md` is the journal (mirrors the pattern used in the
`davinci-resolve-mcp` repo's `RESOLVE_MCP_JOURNAL.md`) — it's read at the
start of a session and appended to at the end, not a one-time README.

## Related setup already in place

- **`superpowers`** Claude Code plugin (user scope, installed 2026-08-03) —
  the skills referenced above (brainstorming, writing-plans,
  test-driven-development, etc.) come from it and are available in every
  session automatically.
- Claude's own memory system also holds a pointer to this repo, so it's
  recognized even from a session that didn't start in this directory —
  naming a project here should be enough.
