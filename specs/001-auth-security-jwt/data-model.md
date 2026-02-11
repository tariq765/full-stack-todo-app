# Data Model: Authentication & Security with JWT

## Entities

### User Identity
**Description**: Represents an authenticated user with unique identifier extracted from JWT payload
**Fields**:
- id (string/UUID): Unique user identifier from JWT payload
- email (string): User's email address from authentication
- name (string, optional): User's display name
- created_at (datetime): Account creation timestamp
- updated_at (datetime): Last update timestamp

**Relationships**:
- One-to-many: User has many Todo items
- One-to-many: User has many Sessions (via JWT tokens)

**Validation**:
- id: Required, UUID format
- email: Required, valid email format
- name: Optional, max 255 characters

### JWT Token
**Description**: Cryptographically signed authentication token containing user identity and expiration information
**Fields**:
- token (string): The JWT token string
- user_id (string/UUID): Reference to authenticated user
- issued_at (datetime): Token creation timestamp
- expires_at (datetime): Token expiration timestamp
- type (string): Token type (access/refresh)
- revoked (boolean): Whether token has been revoked

**Validation**:
- token: Required, valid JWT format
- user_id: Required, must reference existing user
- expires_at: Required, must be in the future
- type: Required, one of ['access', 'refresh']

### Authentication Secret
**Description**: Shared secret key (BETTER_AUTH_SECRET) used by both frontend and backend for signing and verifying JWTs
**Fields**:
- secret_key (string): The secret key value
- algorithm (string): Signing algorithm (default: HS256)
- created_at (datetime): Secret creation timestamp

**Note**: This entity represents configuration rather than stored data.

## State Transitions

### User Authentication Flow
1. Unauthenticated → Authenticating (during login/registration)
2. Authenticating → Authenticated (on successful authentication)
3. Authenticated → Unauthenticated (on logout/expiry)

### JWT Token Lifecycle
1. Not issued → Active (when JWT is created)
2. Active → Expired (when token reaches expiration time)
3. Active → Revoked (when user logs out)

## Access Control Rules

### Data Isolation
- Users can only access their own data
- Backend validates user_id in JWT against requested resources
- All queries must be scoped to authenticated user

### Authorization Checks
- Verify JWT signature using shared secret
- Validate token has not expired
- Confirm user_id in JWT matches requested resource owner
- Return 401 Unauthorized for invalid tokens