from fastapi import Depends, HTTPException, status
from typing import Callable
from ..core.security import verify_token, TokenData


def get_current_user(token_data: TokenData = Depends(verify_token)) -> str:
    """Get the current authenticated user's ID from the token."""
    if not token_data.user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_data.user_id


def validate_user_id_match(path_user_id: str, current_user_id: str = Depends(get_current_user)):
    """Validate that the user_id in the path parameter matches the authenticated user's ID."""
    if path_user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Path user_id does not match authenticated user_id"
        )
    return current_user_id