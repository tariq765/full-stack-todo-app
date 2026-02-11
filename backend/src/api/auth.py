from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional
from ..core.security import create_access_token, verify_token as verify_auth_token
from ..core.config import settings
from ..db.session import get_session
from sqlmodel import Session, select
from ..models.user import User
from passlib.context import CryptContext
import uuid
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/api/auth", tags=["authentication"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    token: str
    user_id: str
    user: Optional[dict] = None

class ErrorResponse(BaseModel):
    message: str

@router.post("/register", response_model=TokenResponse, responses={
    400: {"model": ErrorResponse, "description": "Bad Request - Invalid input or email already registered"}
})
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user with email and password.
    """
    # Check if user already exists
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = pwd_context.hash(user_data.password)

    # Create new user
    user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    # Create access token
    access_token = create_access_token(data={"sub": str(user.id)})

    return TokenResponse(
        token=access_token,
        user_id=str(user.id),
        user={"id": str(user.id), "email": user.email}
    )


@router.post("/login", response_model=TokenResponse, responses={
    401: {"model": ErrorResponse, "description": "Unauthorized - Invalid credentials"}
})
def login(login_data: UserLogin, session: Session = Depends(get_session)):
    """
    Authenticate user and return access token.
    """
    # Find user by email
    user = session.exec(select(User).where(User.email == login_data.email)).first()

    if not user or not pwd_context.verify(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # Create access token
    access_token = create_access_token(data={"sub": str(user.id)})

    return TokenResponse(
        token=access_token,
        user_id=str(user.id),
        user={"id": str(user.id), "email": user.email}
    )


from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

@router.get("/verify", response_model=dict)
def verify_token_endpoint(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verify the authenticity of a token.
    """
    try:
        token_data = verify_auth_token(credentials)
        return {"valid": True, "user_id": token_data.user_id}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )