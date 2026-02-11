from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)


class User(UserBase, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    hashed_password: str


class UserRead(UserBase):
    id: str