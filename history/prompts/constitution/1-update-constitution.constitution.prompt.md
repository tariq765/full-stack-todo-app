---
id: 1
title: Update Constitution
stage: constitution
date: 2026-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Hp
command: /sp.constitution
labels: [constitution, spec-driven-development, security]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---
## Prompt

Project: Todo Full-Stack Web Application (Hackathon Phase-2)

Project Objective

Transform an existing console-based Todo application into a modern, secure, multi-user full-stack web application with persistent storage, authentication, and a responsive user interface, using a fully spec-driven, agentic development workflow.
No manual coding is permitted; all implementation must be generated and iterated via Claude Code and Spec-Kit Plus.

Core Principles

Security First

All API access must be authenticated.

User data isolation is mandatory.

No endpoint may leak or expose another user's data.

Spec-Driven Development

Every implementation decision must be traceable back to an explicit specification.

No undocumented behavior is allowed.

Specs → Plans → Tasks → Code is strictly enforced.

Separation of Concerns

Frontend, backend, authentication, and database layers must be clearly decoupled.

Each layer communicates only through well-defined interfaces.

Deterministic & Reproducible Behavior

Given the same inputs and environment variables, the system must behave identically.

No hidden state or implicit dependencies.

Minimalism with Completeness

Implement only required features, but implement them fully and correctly.

Avoid unnecessary abstractions or overengineering.

Architectural Standards
Frontend

Framework: Next.js 16+ (App Router)

Responsibility:

User authentication via Better Auth

JWT handling and API request authorization

UI rendering and user interaction

Must not:

Contain business logic related to data ownership

Directly access the database

Backend

Framework: FastAPI (Python)

ORM: SQLModel

Responsibility:

Enforce authentication and authorization

Validate JWT tokens

Apply user-based data filtering

Implement all REST API endpoints

Must not:

Manage frontend sessions

Depend on frontend runtime behavior

Database

Engine: Neon Serverless PostgreSQL

Responsibility:

Persistent storage of users and tasks

Enforce schema integrity

Must not:

Store authentication sessions

Contain duplicated or derived data unnecessarily

Authentication & Security Standards

Authentication is implemented using Better Auth on the frontend.

Better Auth must issue JWT tokens.

JWT tokens must:

Be signed using a shared secret (BETTER_AUTH_SECRET)

Contain sufficient user identity information (e.g., user ID, email)

Expire automatically

The backend must:

Verify JWT signature on every request

Reject invalid or missing tokens with 401 Unauthorized

Extract user identity exclusively from the JWT

Route parameters such as {user_id} must be validated against the authenticated user.

API Standards

API style: RESTful

All endpoints require authentication.

All task operations must be scoped to the authenticated user.

Standard HTTP response codes must be used:

200 OK

201 Created

400 Bad Request

401 Unauthorized

404 Not Found

No endpoint may return data belonging to another user.

Development Constraints

No manual coding is allowed.

All code must be generated via Claude Code using Spec-Kit Plus.

Environment configuration must use .env files.

Frontend and backend must share authentication secrets via environment variables.

The system must run locally without additional services beyond:

Next.js

FastAPI

Neon PostgreSQL

Quality Standards

Code must be readable and maintainable.

Folder structure must reflect architectural boundaries.

No unused files, endpoints, or configurations.

Clear error handling and predictable behavior.

Success Criteria

The project is considered successful when:

All 5 basic Todo features are fully implemented as a web application

Multiple users can safely use the system without data leakage

Authentication is enforced on every API request

Backend correctly verifies JWT tokens

Tasks are persisted in Neon PostgreSQL

The full development lifecycle (spec → plan → tasks → code) is clearly demonstrable

Out of Scope

Advanced role-based access control

Real-time updates (WebSockets)

Third-party integrations beyond Better Auth

UI animations or visu

## Response snapshot

Created an updated constitution file at .specify/memory/constitution.md based on the provided specifications for the Todo Full-Stack Web Application. The new constitution incorporates all the core principles including Security First, Spec-Driven Development, Separation of Concerns, Deterministic & Reproducible Behavior, Minimalism with Completeness, and No Manual Coding. It also includes technical architecture standards for Frontend (Next.js 16+), Backend (FastAPI/SQLModel), and Database (Neon Serverless PostgreSQL), along with authentication and security standards, API standards, development constraints, and quality standards.

## Outcome

- ✅ Impact: Updated project constitution with comprehensive principles and standards
- 🧪 Tests: No tests run yet
- 📁 Files: Updated .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: Continue with spec development following the new constitution
- 🧠 Reflection: The constitution now serves as the authoritative guide for the entire development process

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin spec development following the new constitution