from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class Droga(db.Model):
    __tablename__ = "droga"
    
    drogaId = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = False)
    
    def __init__(self, nome):
        self.nome = nome