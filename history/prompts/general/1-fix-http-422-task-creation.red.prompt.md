---
id: 1
title: Fix-HTTP-422-Task-Creation
stage: red
date: 2026-01-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 003-frontend-ux
user: unknown
command: /sp.phr
labels: ["bug-fix", "http-error", "jwt-validation", "task-creation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:/Users/Hp/OneDrive/Desktop/TODO WEB PHASE2/frontend/src/app/dashboard/page.tsx
 - C:/Users/Hp/OneDrive/Desktop/TODO WEB PHASE2/frontend/src/lib/jwt-utils.ts
tests:
 - none
---

## Prompt

todo application mai task add nhi ho raha hai http error 422 aa raha hai please solve this issue
task api.ts ki file check karo errror wohi se aa raha hai

## Response snapshot

Fixed the HTTP 422 error in task creation by ensuring the user ID passed to API endpoints matches the user ID in the JWT token. Created a JWT utility function to decode tokens and extract the user ID from the token payload, ensuring consistency between the frontend and backend validation.

## Outcome

- ✅ Impact: Resolved HTTP 422 error by fixing user ID mismatch between JWT token and API path parameter
- 🧪 Tests: none
- 📁 Files: Modified dashboard page and created JWT utility file
- 🔁 Next prompts: none
- 🧠 Reflection: The issue was caused by inconsistency between user ID in localStorage and JWT token payload

## Evaluation notes (flywheel)

- Failure modes observed: The original code was using a fallback user ID when the token didn't match, causing backend validation to fail
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none