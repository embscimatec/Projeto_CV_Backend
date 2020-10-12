from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.orm import relationship
from app import db
import enum

class Instituicao(db.Model):
    __tablename__ = "instituicao"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(200), nullable = False)
    enderecoId = db.Column(db.Integer, ForeignKey(Endereco.id), nullable = False)
    endereco = db.relationship("Endereco", back_populates = "instituicao")
    pessoa = db.relationship("Pessoa", back_populates = "instituicao")
    
    def __init__(self, nome, email, senha, enderecoId):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.enderecoId = enderecoId