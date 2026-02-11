from sqlmodel import create_engine
from ..core.config import settings

# Create database engine
if settings.DATABASE_URL and "sqlite://" in settings.DATABASE_URL.lower():
    # SQLite-specific connect args
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
        echo=True  # Set to False in production
    )
else:
    # PostgreSQL or other database connect args
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        echo=True  # Set to False in production
    )


def get_session():
    from sqlmodel import Session
    with Session(engine) as session:
        yield session