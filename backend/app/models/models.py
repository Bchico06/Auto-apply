from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, default="")
    desired_role = Column(String, default="")
    years_experience = Column(Integer, default=0)
    location = Column(String, default="")
    work_mode = Column(String, default="remote")
    languages = Column(String, default="")
    skills = Column(Text, default="")

class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    platform = Column(String, nullable=False)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    status = Column(String, default="sent")
    interview = Column(Boolean, default=False)
    user = relationship("User")
