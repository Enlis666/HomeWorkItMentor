from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings
from sqlalchemy import create_engine

engine = create_engine(
    url=settings.DATABASE_URL_psycopg2,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
