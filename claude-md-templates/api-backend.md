# [API Name]

## What This Is
[What does this API do? Who calls it?]

## Stack
- Runtime: [e.g., Node.js 20 / Python 3.12]
- Framework: [e.g., Express / FastAPI]
- Database: [e.g., PostgreSQL / MongoDB]
- Auth: [e.g., JWT — tokens expire in 24h]

## Commands
- Start: npm start (or: uvicorn main:app --reload)
- Test: npm test (or: pytest)
- Lint: npm run lint (or: ruff check .)

## API Conventions
- REST: GET /resources, POST /resources, PATCH /resources/:id
- All errors return: { error: string, code: string, status: number }
- Auth header: Authorization: Bearer <token>

## Do Not Touch
- src/generated/ — auto-generated from schema
- db/migrations/ — use migration commands only
