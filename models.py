from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    feedback = Column(Text)
