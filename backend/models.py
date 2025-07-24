from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    progress = relationship("UserProgress", back_populates="user")

class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    completed_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="progress")
    problem = relationship("Problem")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True)
    language = Column(String, index=True) # ✨ 언어 필드 추가
    slug = Column(String, index=True)
    title = Column(String)
    problems = relationship("Problem", back_populates="chapter")

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    problem_number_in_chapter = Column(Integer)
    title = Column(String)
    question = Column(Text)
    theory = Column(Text)
    chapter = relationship("Chapter", back_populates="problems")