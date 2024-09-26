from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = "tb_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    description = Column(String(90))
    price = Column(Integer)