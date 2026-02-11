---
id: 1
title: "Fix-HTTP-422-error-in-task-creation"
stage: "red"
date: "2026-01-31"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "todo-app"
branch: "003-frontend-ux"
user: "Hp"
command: "manual"
labels: ["debugging", "authentication", "http-error", "frontend", "backend"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "frontend/src/app/dashboard/page.tsx"
tests: []
---

# Fix HTTP 422 error in task creation

## Context

User reported HTTP 422 error when trying to add tasks to the Todo Web application. The error was occurring due to an authentication mismatch between the user ID in the JWT token and the user ID in the API request path.

## Analysis

Investigated the codebase and found that the issue was in the dashboard page where a fallback mechanism was returning 'mock-user-id' when token extraction failed, causing authentication failures in the backend API.

## Solution

Modified the frontend code in `frontend/src/app/dashboard/page.tsx` to properly handle authentication failures by redirecting to the login page instead of using mock user IDs. Updated all API interaction functions to validate both token and user ID before making requests.

## Outcome & Impact

The fix resolves the HTTP 422 error by ensuring the user ID in the JWT token always matches the user ID in API requests, eliminating the authentication mismatch that was causing the error.

## Tests Summary

Manual testing confirmed that the authentication flow now properly handles invalid tokens by redirecting to the login page.

## Files Summary

- `frontend/src/app/dashboard/page.tsx` - Fixed authentication handling and improved error checking

## Next Prompts

None needed - the issue has been resolved.

## Reflection Note

Proper authentication validation is critical for API interactions, and fallback mechanisms should not bypass security checks.

---
Failure modes observed: None
Next experiment to improve prompt quality: None
---