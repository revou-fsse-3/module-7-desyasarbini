from models.base import Base
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from flask_login import UserMixin
import bcrypt


class User(Base, UserMixin):
    __tablename__ = 'user'

    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    password = mapped_column(String(100), nullable=False)
    

    def __repr__(self):
        return f'<User {self.name}>'
    
    # u/ hash atau mengubah password agar ter encrypt
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # u/ check password login apakah sama dengan yg didatabase
    # password login di hashing dulu lalu disamakan dengan db
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))