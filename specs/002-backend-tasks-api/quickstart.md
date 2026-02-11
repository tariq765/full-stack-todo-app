# Quickstart Guide: Backend API & Database

## Overview
This guide provides a step-by-step walkthrough of the Todo backend API with user-scoped task management and data isolation.

## Prerequisites
- Python 3.11+ installed
- PostgreSQL connection (Neon Serverless)
- Authentication system (from Spec 1) providing JWT tokens

## Setup Steps

### 1. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Set the database connection
export DATABASE_URL="postgresql://username:password@host:port/database_name"
```

### 2. Install Dependencies
```bash
pip install fastapi sqlmodel pyjwt python-multipart uvicorn
```

### 3. Start the Service
```bash
uvicorn main:app --reload
```

## API Flow Walkthrough

### Authentication Required
1. All endpoints require a valid JWT token in the Authorization header
2. Token must contain valid user identity information
3. Request format: `Authorization: Bearer YOUR_JWT_TOKEN`

### Create a Task
1. Make POST request to `/api/{user_id}/tasks`
2. Token user_id must match the path parameter
3. Provide task data in request body
4. Backend assigns ownership to authenticated user
5. Task is stored in database with user_id association

### List User's Tasks
1. Make GET request to `/api/{user_id}/tasks`
2. Backend validates authentication and user ID match
3. Database query filters by authenticated user_id
4. Response contains only user's own tasks

### Update Task
1. Make PUT request to `/api/{user_id}/tasks/{id}`
2. Backend validates user owns the task
3. Updates allowed only for user's own tasks
4. Returns updated task data

### Delete Task
1. Make DELETE request to `/api/{user_id}/tasks/{id}`
2. Backend validates user owns the task
3. Removes task from database
4. Returns success confirmation

## Testing the Flow

### Manual Testing
```bash
# Get user's tasks (assuming valid JWT token)
curl -X GET http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"

# Create a new task
curl -X POST http://localhost:8000/api/user123/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -d '{"title": "New Task", "description": "Task description"}'

# Update a task
curl -X PUT http://localhost:8000/api/user123/tasks/task456 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -d '{"title": "Updated Task", "completed": true}'
```

### Expected Results
- Authenticated requests with valid JWT should return 200 OK
- Requests with invalid/missing JWT should return 401 Unauthorized
- Users can only access their own tasks
- Attempts to access other users' tasks return 401 Unauthorized
- Successful operations return appropriate data/status codes

## Troubleshooting

### Common Issues
- **401 Unauthorized**: Check JWT token validity and format
- **404 Not Found**: Verify task exists and belongs to authenticated user
- **500 Internal Server Error**: Check database connectivity and configuration

### Debugging Steps
1. Verify that environment variables are set correctly
2. Confirm JWT token contains correct user identity
3. Check that database connection is working
4. Review backend logs for authentication and authorization errors