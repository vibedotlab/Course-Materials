# Playwright MCP

Browser automation — let Claude control a browser, take screenshots, fill forms, and test web flows.

## Install

**Mac / Linux:**
```bash
claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest
```

**Windows:**
```bash
claude mcp add --transport stdio playwright -- cmd /c npx -y @playwright/mcp@latest
```

## Verify

```bash
claude mcp list
```

You should see `playwright` in the list.

## Share with your team (optional)

**Mac / Linux:**
```bash
claude mcp add --scope project --transport stdio playwright -- npx -y @playwright/mcp@latest
```

## Remove

```bash
claude mcp remove playwright
```

## What you can do once installed

- "Open my app at localhost:3000 and take a screenshot"
- "Fill out the signup form and click submit"
- "Test the checkout flow end to end"
- "Check that the login page redirects correctly after auth"
