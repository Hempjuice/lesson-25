from sqlalchemy import Column, Integer, String
from models.database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, default="", server_default="")
