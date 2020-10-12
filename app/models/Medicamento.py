from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class Medicamento(db.Model):
    __tablename__ = "medicamento"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    
    def __init__(self, nome):
        self.nome = nome