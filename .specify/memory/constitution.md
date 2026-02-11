<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Added sections: Security First, Spec-Driven Development, Separation of Concerns, Deterministic & Reproducible Behavior, Minimalism with Completeness, Frontend/Backend/Database responsibilities, Authentication & Security Standards, API Standards, Development Constraints, Quality Standards
Modified principles: N/A (new constitution)
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/phr-template.prompt.md ⚠ pending
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### Security First
All API access must be authenticated. User data isolation is mandatory. No endpoint may leak or expose another user's data.

### Spec-Driven Development
Every implementation decision must be traceable back to an explicit specification. No undocumented behavior is allowed. Specs → Plans → Tasks → Code is strictly enforced.

### Separation of Concerns
Frontend, backend, authentication, and database layers must be clearly decoupled. Each layer communicates only through well-defined interfaces.

### Deterministic & Reproducible Behavior
Given the same inputs and environment variables, the system must behave identically. No hidden state or implicit dependencies.

### Minimalism with Completeness
Implement only required features, but implement them fully and correctly. Avoid unnecessary abstractions or overengineering.

### No Manual Coding
All implementation must be generated via Claude Code using Spec-Kit Plus. No manual coding is permitted.

## Technical Architecture Standards

### Frontend
Framework: Next.js 16+ (App Router)
Responsibilities: User authentication via Better Auth, JWT handling and API request authorization, UI rendering and user interaction
Must not: Contain business logic related to data ownership, Directly access the database

### Backend
Framework: FastAPI (Python), ORM: SQLModel
Responsibilities: Enforce authentication and authorization, Validate JWT tokens, Apply user-based data filtering, Implement all REST API endpoints
Must not: Manage frontend sessions, Depend on frontend runtime behavior

### Database
Engine: Neon Serverless PostgreSQL
Responsibilities: Persistent storage of users and tasks, Enforce schema integrity
Must not: Store authentication sessions, Contain duplicated or derived data unnecessarily

## Authentication & Security Standards

Authentication is implemented using Better Auth on the frontend. Better Auth must issue JWT tokens.
JWT tokens must be signed using a shared secret (BETTER_AUTH_SECRET), contain sufficient user identity information (e.g., user ID, email), and expire automatically.
The backend must verify JWT signature on every request, reject invalid or missing tokens with 401 Unauthorized, extract user identity exclusively from the JWT, and validate route parameters such as {user_id} against the authenticated user.

## API Standards

API style: RESTful. All endpoints require authentication. All task operations must be scoped to the authenticated user. Standard HTTP response codes must be used: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found. No endpoint may return data belonging to another user.

## Development Constraints

No manual coding is allowed. All code must be generated via Claude Code using Spec-Kit Plus. Environment configuration must use .env files. Frontend and backend must share authentication secrets via environment variables. The system must run locally without additional services beyond Next.js, FastAPI, and Neon PostgreSQL.

## Quality Standards

Code must be readable and maintainable. Folder structure must reflect architectural boundaries. No unused files, endpoints, or configurations. Clear error handling and predictable behavior.

## Governance

This constitution supersedes all other development practices. All implementation must comply with these principles. Amendments require explicit documentation and approval. Version: 1.0.0 represents the initial ratification of these principles for the Todo Full-Stack Web Application project. All development work must be traceable back to explicit specifications following the Specs → Plans → Tasks → Code workflow.

**Version**: 1.0.0 | **Ratified**: 2026-01-27 | **Last Amended**: 2026-01-27
