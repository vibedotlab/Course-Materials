# [App Name]

## What This Is
[What does it do? Who pays for it?]

## Stack
- Frontend: Next.js 14, TypeScript, Tailwind CSS
- Backend: Node.js, Express, Prisma
- Database: PostgreSQL (Supabase)
- Auth: Clerk
- Payments: Stripe
- Hosting: Vercel (frontend), Railway (backend)

## Commands
- Dev: npm run dev
- Test: npm test
- DB migration: npx prisma migrate dev
- Build: npm run build

## Rules
- TypeScript strict — no `any` types
- React Server Components where possible; Client Components marked 'use client'
- All API calls through app/api/ routes only
- Never bypass Clerk auth middleware
- Stripe webhooks in app/api/webhooks/stripe.ts — already tested, don't touch

## Do Not Touch
- prisma/migrations/ — auto-generated
- app/api/webhooks/ — fragile, already tested
