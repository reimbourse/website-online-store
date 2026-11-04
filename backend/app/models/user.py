from datetime import datetime

from sqlalchemy import Column, DateTime, String

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
