from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class High_Score(Base):
    __tablename__ = "High_Score"
    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    score = Column(Integer)
