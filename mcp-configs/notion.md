# Notion MCP

Read and write Notion pages from inside Claude Code.

## Install

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

## Verify

```bash
claude mcp list
```

You should see `notion` in the list with status `connected`.

## Share with your team (optional)

```bash
claude mcp add --scope project --transport http notion https://mcp.notion.com/mcp
```

## Remove

```bash
claude mcp remove notion
```

## What you can do once installed

- "Read my Notion page titled 'Project Brief'"
- "Add a new row to my Notion database"
- "Create a new page in my workspace"
- "Search for pages mentioning 'Q4 roadmap'"
