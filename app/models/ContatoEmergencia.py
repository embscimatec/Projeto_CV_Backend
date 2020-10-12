from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class ContatoEmergencia(db.Model):
    __tablename__ = "contatoEmergencia"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    relacao = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    
    def __init__(self, nome, relacao, email):
        self.nome = nome
        self.relacao = relacao
        self.email = email
    