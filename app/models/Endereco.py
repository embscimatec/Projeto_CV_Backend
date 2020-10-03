from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class Endereco(db.Model):
    __tablename__ = "endereco"
    
    enderecoId = db.Column(db.Integer, primary_key = True)
    cep = db.Column(db.String, nullable = True)
    logradouro = db.Column(db.String, nullable = False)
    numero = db.Column(db.Integer, nullable = True)
    bairro = db.Column(db.String, , nullable = False)
    cidade = db.Column(db.String, nullable = False)
    estado = db.Column(db.String, nullable = False)
    complemento = db.Column(db.String, nullable = True)
    
    def __init__(self, cep, logradouro, numero, bairro, cidade, estado, complemento):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.complemento = complemento
        
    def __repr__(self):
        return "<User %r>" &% self.cep

    def criarEndereco():
        db.create_all()