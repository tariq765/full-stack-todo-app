# Todo Full-Stack Web Application

This is a complete full-stack Todo application with authentication, user-scoped task management, and secure data persistence.

## Project Structure

```
├── backend/                 # FastAPI backend with SQLModel ORM
│   ├── src/
│   │   ├── main.py         # Main application entry point
│   │   ├── models/         # Database models (SQLModel)
│   │   ├── services/       # Business logic
│   │   ├── api/            # API routes
│   │   └── core/           # Configuration and security
│   ├── requirements.txt    # Python dependencies
│   └── run_backend.py      # Backend startup script
├── specs/                  # Specification files
│   └── 002-backend-tasks-api/
├── .env                    # Environment variables (not tracked)
├── .env.example            # Environment template
└── .gitignore             # Git ignore rules
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Copy `.env.example` to `.env` and update the values:
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Run the Backend**:
   ```bash
   python run_backend.py
   # Or alternatively: uvicorn src.main:app --reload
   ```

### Frontend Setup (Separate Application)

The frontend is a separate Next.js application that would typically run on port 3000:

1. **Navigate to frontend directory** (when created):
   ```bash
   cd frontend  # This directory doesn't exist yet in this backend-only implementation
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Run the Frontend**:
   ```bash
   npm run dev
   # Runs on http://localhost:3000
   ```

## API Endpoints

The backend API runs on `http://localhost:8000` and provides:

- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task for a user
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Ports

- **Backend API**: `http://localhost:8000`
- **Frontend** (when implemented): `http://localhost:3000`
- **Database**: Neon PostgreSQL (cloud-based)

## Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+
- **SQLModel**: SQL databases in Python, with full support for SQLAlchemy and Pydantic
- **PyJWT**: Implementation of the JSON Web Token standard
- **Uvicorn**: Lightning-fast ASGI server

### Authentication & Security
- **Better Auth**: Authentication system (configured in frontend)
- **JWT Tokens**: Secure authentication tokens
- **User Scoping**: Each user can only access their own data

### Database
- **Neon PostgreSQL**: Cloud-based PostgreSQL database with serverless capabilities