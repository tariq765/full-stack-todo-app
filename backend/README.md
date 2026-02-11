# Todo Backend API

This is the backend API for the Todo application, providing secure, user-scoped task management with data persistence in Neon Serverless PostgreSQL.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Copy `.env.example` to `.env` and update the values:
   ```bash
   cp ../.env.example ../.env
   # Edit ../.env with your actual values
   ```

3. **Run the Application**:
   Option 1: Using the run pscript
   ```bash
   cd backend
   python run_backend.py
   ```

   Option 2: Using uvicorn directly
   ```bash
   cd 
   backend
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints

The API provides the following endpoints for task management:

- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task for a user
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Port Information

- **Backend API**: Runs on `http://localhost:8000`
- **Frontend**: Typically runs on `http://localhost:3000` (separate Next.js application)

## Technologies Used

- FastAPI: Modern, fast web framework for building APIs with Python 3.7+
- SQLModel: SQL databases in Python, with full support for SQLAlchemy and Pydantic
- PyJWT: Implementation of the JSON Web Token standard
- Uvicorn: Lightning-fast ASGI server