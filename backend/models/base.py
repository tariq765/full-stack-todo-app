from sqlmodel import SQLModel


class Base(SQLModel):
    """
    Base class for all database models.
    Currently just extends SQLModel for future extensibility.
    """
    pass