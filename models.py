from email.policy import default
from database import Base
from sqlalchemy import Boolean, Integer, String, Column, Text


class Item(Base):
    # create table
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique = True)
    price = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    isActive = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"