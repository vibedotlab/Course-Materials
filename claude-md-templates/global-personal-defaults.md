# My Personal Defaults

Save this as `~/.claude/CLAUDE.md` (the `~` means your home folder).
It applies automatically to every project you open — no per-project setup needed.

---

## Who I Am
- I am [describe yourself — e.g., "a non-technical founder building a SaaS app"]
- My experience level: [e.g., "complete beginner" / "can read code but not write it"]

---

## How I Work
- I prefer TypeScript over JavaScript
- I don't like verbose code — be concise
- Never hardcode secrets — use env vars
- Prefer editing existing files over creating new ones

## Communication
- Skip explaining things I can read from the code
- Ask clarifying questions before starting complex tasks
- Tell me when you're uncertain rather than guessing confidently

## Workflow
- Run lint and tests after changes
- Commit often with descriptive messages
- One task per session — use /clear between tasks

---

## Advanced Behaviors

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep the main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from me: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until the mistake rate drops
- Review lessons at session start for the relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from me
- Go fix failing CI tests without being told how

---

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in with me before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

---

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **No Surprises**: Tell me before doing anything irreversible (deleting files, pushing to git, dropping data)
- **Honesty**: If you don't know, say so. Don't invent answers or fake confidence.

---

## Safety
- NEVER commit .env files or expose credentials in any form
- Ask before executing any destructive command (rm, git push --force, docker run)
- Do not read or suggest values from .env, secrets.json, or credential files

## Things to Never Do
- Never delete files without asking me first
- Never push to git without my confirmation
- Never make changes outside the scope of what I asked
- Never ignore an explicit instruction I've given
