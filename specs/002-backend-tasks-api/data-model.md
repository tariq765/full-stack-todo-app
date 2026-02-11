# Data Model: Backend API & Database

## Entities

### Task
**Description**: Represents a user's task with fields: id, title, description, completed status, user_id, timestamps
**Fields**:
- id (Integer, Primary Key): Unique task identifier (auto-generated)
- title (String): Task title (required, max 255 characters)
- description (String, optional): Task details (optional, max 1000 characters)
- completed (Boolean): Completion status (default: False)
- user_id (String): Owner's user ID (required, from JWT token)
- created_at (DateTime): Creation timestamp (auto-generated)
- updated_at (DateTime): Last update timestamp (auto-generated)

**Relationships**:
- Many-to-one: Task belongs to one User (via user_id foreign key)

**Validation**:
- title: Required, max 255 characters
- description: Optional, max 1000 characters
- completed: Boolean, default False
- user_id: Required, must match authenticated user from JWT

### User (Reference)
**Description**: Represents the authenticated user whose identity is extracted from JWT token
**Fields**:
- id (String): Unique user identifier from JWT payload
- email (String): User's email address from authentication
- name (String): User's display name

**Note**: User data is managed by the authentication system (Spec 1), referenced by user_id in Task.

## State Transitions

### Task Lifecycle
1. Not created → Pending creation (when POST request received)
2. Pending creation → Active (after successful database insertion)
3. Active → Updated (after PUT/PATCH request)
4. Active/Updated → Deleted (after DELETE request)

### Task Completion States
1. Completed = False → Task is pending/incomplete
2. Completed = True → Task is completed
3. PATCH request → Toggles between True and False

## Access Control Rules

### Data Isolation
- Each task is associated with exactly one user via user_id
- All database queries must filter by authenticated user_id
- No task should be accessible by a user other than its owner

### Authorization Checks
- Verify JWT token is valid and not expired
- Confirm user_id in JWT matches requested resource owner
- Return 401 Unauthorized for invalid or mismatched user access
- Return 404 Not Found for tasks that exist but belong to other users