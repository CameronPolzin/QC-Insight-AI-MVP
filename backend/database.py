from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#SQLite DB file location
DATABASE_URL = "sqlite:///./qc_reports.db"

#creates the database engine/connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#creates DB sessions used to read/write data
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#base class used by SQLAlchemy models
Base = declarative_base()