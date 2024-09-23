from sqlalchemy import Column, Integer, String, Float
from ..schemas.database import Base


class API_KEY(Base):
    __tablename__ = "apikey"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True)

