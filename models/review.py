from models.base import Base
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Review(Base):
    __tablename__ = 'book_review'

    id = mapped_column(Integer, primary_key=True)
    book_id = mapped_column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    email = mapped_column(String(30), nullable= False)
    rating = mapped_column(Integer)
    review_content = mapped_column(Text)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f'<Review {self.id}>'