from sqlalchemy import Column, String

from app.core.database import Base


class Category(Base):
    __tablename__ = "categories"

    name = Column(String, nullable=False)
    slug = Column(String, unique=True)


class Collection(Base):
    __tablename__ = "collections"

    name = Column(String, nullable=False)
    slug = Column(String, unique=True)
    season = Column(String)
