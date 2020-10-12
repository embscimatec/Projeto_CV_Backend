from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class Funcionario(db.Model):
    __tablename__ = "funcionario"
    
    id = db.Column(db.Integer, primary_key = True)
    senha = db.Column(db.String, nullable = False)
    # Falta criar relação com pessoa
    
    def __init__(self, senha):
        self.senha = senha