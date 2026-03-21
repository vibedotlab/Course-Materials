# Vibecoding with Claude Code — Course Materials

Free companion files for the course. Everything used to build it, and everything you need to replicate it.

Browse the folders below or click **Code → Download ZIP** to grab everything at once.

---

## What's Here

| Folder | Contents |
|---|---|
| [claude-md-templates/](claude-md-templates/) | 7 ready-to-paste CLAUDE.md files — one for each project type |
| [skills/](skills/) | 6 skill files you can drop into any project |
| [agents/](agents/) | Custom agent used to research and build this course |
| [mcp-configs/](mcp-configs/) | Verified MCP install commands for 5 popular tools |
| [skills/md-to-pdf/scripts/](skills/md-to-pdf/scripts/) | Python + CSS scripts for converting Markdown to PDF |

---

## How to Use

**Option A — Download everything:**
Click the green **Code** button above → **Download ZIP** → unzip and copy what you need.

**Option B — Copy a single file:**
Click any file → click the **Copy raw file** button (top right of the file view).

**Option C — Clone the repo:**
```bash
git clone https://github.com/vibedotlab/Course-Materials
```

---

## CLAUDE.md Templates

These are ready-to-use instruction files for Claude. Copy one, rename it `CLAUDE.md`, drop it in your project root, and fill in the bracketed placeholders.

| File | Use it for |
|---|---|
| [generic-starter.md](claude-md-templates/generic-starter.md) | Any project — minimal, fill in your stack |
| [generic-starter-full.md](claude-md-templates/generic-starter-full.md) | Any project — full version with behaviors, patterns, output standards |
| [saas-web-app.md](claude-md-templates/saas-web-app.md) | Next.js + Postgres + Stripe |
| [content-course.md](claude-md-templates/content-course.md) | Courses, books, content projects |
| [api-backend.md](claude-md-templates/api-backend.md) | REST APIs (Node.js or Python) |
| [data-automation.md](claude-md-templates/data-automation.md) | Python data + automation scripts |
| [global-personal-defaults.md](claude-md-templates/global-personal-defaults.md) | Save to `~/.claude/CLAUDE.md` — applies to every project |

**To use:** Copy the file → rename it `CLAUDE.md` → drop it in your project root → fill in the bracketed placeholders.

---

## Skills

Skills are reusable workflows you install once and trigger with a slash command (e.g. `/commit`, `/review`).

| File | What it does |
|---|---|
| [skills/commit.md](skills/commit.md) | Runs lint + tests, writes a proper commit message, stages and commits |
| [skills/review.md](skills/review.md) | Reviews a branch diff for logic errors, security issues, missing tests |
| [skills/research.md](skills/research.md) | Searches docs + community, writes a research brief to /research/ |
| [skills/course-writer.md](skills/course-writer.md) | Writes a course chapter: research → outline → draft → quality check → save |
| [skills/svg-diagram/](skills/svg-diagram/) | Generates clean SVG architecture and flow diagrams from a description |
| [skills/md-to-pdf/](skills/md-to-pdf/) | Converts markdown files to a professionally styled PDF |

**To install a skill:**
1. Create `.claude/skills/` in your project root (or `~/.claude/skills/` for global use)
2. Copy the `.md` file into that folder
3. Start a new Claude Code session — it auto-discovers skills

---

## Agents

Custom subagents that Claude Code can spawn to handle specialized tasks autonomously.

| File | What it does |
|---|---|
| [agents/researcher.md](agents/researcher.md) | Deep web researcher — searches Anthropic docs + community, returns a verified research brief |

**To install an agent:**
1. Create `.claude/agents/` in your project root (or `~/.claude/agents/` for global use)
2. Copy the `.md` file into that folder
3. Claude Code will discover and use it automatically when relevant

---

## MCP Configs

MCPs (Model Context Protocol) give Claude access to external tools — GitHub, Notion, databases, and more. Each file has the exact install command.

| File | MCP it installs |
|---|---|
| [mcp-configs/github.md](mcp-configs/github.md) | GitHub — read issues, create PRs, manage repos |
| [mcp-configs/notion.md](mcp-configs/notion.md) | Notion — read and write pages |
| [mcp-configs/sentry.md](mcp-configs/sentry.md) | Sentry — debug production errors |
| [mcp-configs/playwright.md](mcp-configs/playwright.md) | Playwright — browser automation |
| [mcp-configs/postgresql.md](mcp-configs/postgresql.md) | PostgreSQL — direct database access |

Each file has the exact install command and notes on what it does.

---

## Scripts (md-to-pdf)

Standalone scripts used by the md-to-pdf skill to convert Markdown courses to PDF.

| File | What it does |
|---|---|
| [skills/md-to-pdf/scripts/assemble.py](skills/md-to-pdf/scripts/assemble.py) | Assembles multiple `.md` files into one document for pandoc, fixes image paths, adds cover page |
| [skills/md-to-pdf/scripts/course.css](skills/md-to-pdf/scripts/course.css) | Professional course CSS for pandoc + weasyprint — colors, typography, code blocks, callouts |

**To use the scripts directly:**
```bash
# 1. Assemble all .md files into one
python assemble.py ./chapters output.md --title "My Course" --author "Your Name"

# 2. Convert to PDF
pandoc output.md -o course.pdf --pdf-engine=weasyprint --css=course.css --toc --standalone
```

---

## Links

- Course: [Vibecoding with Claude Code](https://vibedotlab.com)
- Official Claude Code docs: https://docs.anthropic.com/en/docs/claude-code
- MCP registry: https://modelcontextprotocol.io
- Official skills repo: https://github.com/anthropics/skills
