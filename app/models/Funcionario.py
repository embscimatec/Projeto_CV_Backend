from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db
from sqlalchemy.orm import relationship

class Funcionario(db.Model):
    __tablename__ = "funcionario"
    
    id = db.Column(db.Integer, primary_key = True)
    senha = db.Column(db.String, nullable = False)

    # Relação com pessoa
    pessoaId = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key = True)
    pessoa = relationship("Pessoa", back_populates = "funcionario")
    
    
    def __init__(self, senha, pessoa, pessoaId):
        self.senha = senha
        self.pessoa = pessoa
        self.pessoaId = pessoaId