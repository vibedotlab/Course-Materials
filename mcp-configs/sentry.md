# Sentry MCP

Connect Claude to your Sentry error monitoring. Debug production errors without leaving your editor.

## Install

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

## Verify

```bash
claude mcp list
```

You should see `sentry` in the list with status `connected`.

## Share with your team (optional)

```bash
claude mcp add --scope project --transport http sentry https://mcp.sentry.dev/mcp
```

## Remove

```bash
claude mcp remove sentry
```

## What you can do once installed

- "Show me the latest errors in my Sentry project"
- "What's causing the TypeError spike in production?"
- "Summarize the errors from the last 24 hours"
- "Help me fix the top error by stack count"
