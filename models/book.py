from models.base import Base
from sqlalchemy import Integer, String, Text, DateTime, func
from sqlalchemy.orm import mapped_column, relationship, backref
from sqlalchemy.sql import func


class Book(Base):
    __tablename__ = 'book'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(191), nullable=False)
    price = mapped_column(Integer)
    description = mapped_column(Text)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship list
    reviews= relationship("Review", cascade="all,delete-orphan")

    def __repr__(self):
        return f'<Book {self.name}>'