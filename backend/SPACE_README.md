# Todo App Backend

This is a FastAPI-based backend for the Todo application, deployed on Hugging Face Spaces.

## Features
- User authentication (registration & login)
- Task management (create, read, update, delete)
- JWT-based authentication
- SQLModel with SQLite database

## Endpoints
- `/api/auth/register` - Register new user
- `/api/auth/login` - Login existing user
- `/api/auth/verify` - Verify JWT token
- `/api/{user_id}/tasks` - Manage user tasks

## Configuration
The application uses environment variables for configuration:
- `SECRET_KEY` - Secret key for JWT signing
- `ALGORITHM` - Algorithm for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time (default: 30 days)

## Local Development
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Deployed on Hugging Face Spaces
This application is designed to run on Hugging Face Spaces with automatic scaling and management.