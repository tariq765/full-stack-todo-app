# Research: Authentication & Security with JWT

## Decision Log

### Decision: Technology Stack Selection
**Rationale**: Based on the constitution, we'll use:
- Frontend: Next.js 16+ (App Router) with Better Auth
- Backend: FastAPI (Python) with SQLModel ORM
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth for JWT issuance and verification

### Decision: Project Structure
**Rationale**: Following the constitution's separation of concerns:
- Frontend: Next.js app with authentication handling
- Backend: FastAPI with JWT validation middleware
- Shared: Environment variables for authentication secrets

### Decision: JWT Implementation Approach
**Rationale**:
- Use Better Auth on frontend to handle user registration/login
- Issue JWT tokens with user identity and expiration
- Share authentication secret (BETTER_AUTH_SECRET) between frontend and backend
- Backend validates JWT on every request and enforces data access controls

### Decision: Data Isolation Strategy
**Rationale**:
- Backend extracts user ID from JWT payload
- All API endpoints validate that requested resources belong to authenticated user
- Database queries are filtered by authenticated user ID

## Best Practices Researched

### JWT Security Best Practices
- Use strong secrets for signing (BETTER_AUTH_SECRET)
- Set reasonable expiration times (15 min for access tokens, 7 days for refresh tokens)
- Validate all JWT claims (iss, exp, aud)
- Implement proper error handling for invalid tokens

### Better Auth Integration
- Configure Better Auth client on frontend
- Set up API routes for authentication endpoints
- Handle token refresh automatically
- Implement proper logout functionality

### FastAPI JWT Middleware
- Create dependency for JWT validation
- Extract user identity from token payload
- Return 401 Unauthorized for invalid tokens
- Integrate with FastAPI's security features

## Unknowns Resolved

### Language/Version: NEEDS CLARIFICATION
**Resolved**:
- Frontend: TypeScript with Next.js 16+
- Backend: Python 3.11+ with FastAPI

### Primary Dependencies: NEEDS CLARIFICATION
**Resolved**:
- Frontend: @better-auth/react, @better-auth/client, next
- Backend: fastapi, sqlmodel, pyjwt, python-multipart

### Storage: NEEDS CLARIFICATION
**Resolved**:
- Primary: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens stored client-side

### Testing: NEEDS CLARIFICATION
**Resolved**:
- Frontend: Jest/React Testing Library for components
- Backend: pytest for API tests
- Integration: End-to-end tests with Playwright

### Target Platform: NEEDS CLARIFICATION
**Resolved**:
- Frontend: Web application (Next.js) targeting modern browsers
- Backend: API server running on Python environment

### Performance Goals: NEEDS CLARIFICATION
**Resolved**:
- API response time: <200ms p95
- JWT validation: <50ms
- Authentication endpoints: <100ms

### Constraints: NEEDS CLARIFICATION
**Resolved**:
- <200ms p95 response time for API endpoints
- <100MB memory usage for backend
- Offline capability not required (web app)

### Scale/Scope: NEEDS CLARIFICATION
**Resolved**:
- Support up to 10,000 concurrent users
- Handle up to 1,000 requests per second
- Support typical Todo application use cases