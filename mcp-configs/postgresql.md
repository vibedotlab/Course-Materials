# PostgreSQL MCP

Give Claude direct read access to your PostgreSQL database. Useful for debugging, data analysis, and generating queries.

## Install

Replace `postgresql://user:pass@host/dbname` with your actual connection string:

```bash
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://user:pass@host/dbname"
```

**Example with a local database:**
```bash
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://postgres:password@localhost:5432/myapp"
```

## Verify

```bash
claude mcp list
```

You should see `db` in the list.

## Remove

```bash
claude mcp remove db
```

## Security note

- Never commit your connection string to git
- Use a read-only database user where possible
- For production databases, use environment variables to store credentials

## What you can do once installed

- "Show me the schema of the users table"
- "How many signups happened in the last 7 days?"
- "Find users who haven't logged in for 30 days"
- "Write a query to find the top 10 products by revenue"
