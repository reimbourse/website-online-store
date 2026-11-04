from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.core.database import Base, UUIDIdMixin


class User(Base, UUIDIdMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
