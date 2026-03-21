# GitHub MCP

Read issues, create pull requests, manage repositories — all from inside Claude Code.

## Install

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

## Verify

```bash
claude mcp list
```

You should see `github` in the list with status `connected`.

## Share with your team (optional)

Add `--scope project` to save the config to `.mcp.json` (checked into git):

```bash
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/
```

## Remove

```bash
claude mcp remove github
```

## What you can do once installed

- "List open issues in this repo"
- "Create a PR from this branch to main"
- "Show me recent commits on the main branch"
- "Close issue #42 with a comment"
