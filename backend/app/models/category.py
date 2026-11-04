from sqlalchemy import Column, String

from app.core.database import Base, UUIDIdMixin


class Category(Base, UUIDIdMixin):
    __tablename__ = "categories"

    name = Column(String, nullable=False)
    slug = Column(String, unique=True)


class Collection(Base, UUIDIdMixin):
    __tablename__ = "collections"

    name = Column(String, nullable=False)
    slug = Column(String, unique=True)
    season = Column(String)
