from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.orm import relationship
from app import db
import enum

class EnumSexo(enum.Enum):
    Feminino = "F"
    Masculino = "M"
    Indefinido = "I"

class Pessoa(Db.Model):
    __tablename__ = "pessoa"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    sobrenome = db.Column(db.String(20), nullable = False)
    sexo = db.Column(db.Enum('F', 'M', 'I', name="enumgeneros"), default = 'I', nullable = False)
    cpf = db.Column(db.String(14), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    data_nascimento = db.Column(db.DateTime, nullable = False)
    irmao_gemeo = db.Column(db.Boolean, default = False, nullable = False)
    enderecoId = db.Column(db.Integer, db.ForeignKey(Endereco.id), nullable = False)
    imagemId = = db.Column(db.Integer, db.ForeignKey(Imagem.id), nullable = False)
    instituicaoId = db.Column(db.Integer, db.ForeignKey(Instituicao.id), nullable = False)
    endereco = db.relationship("Endereco", back_populates = "pessoa")
    imagem = db.relationship("Imagem", back_populates = "pessoa")
    instituicao = db.relationship("Instituicao", back_populates = "pessoa")
    
    def __init__(self, nome, sobrenome, sexo, cpf, data_nasc, email, gemeo, enderecoId, imagemId, instituicaoId):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nasc
        self.irmao_gemeo = gemeo
        self.enderecoId = enderecoId
        self.imagemId = imagemId
        self.instituicaoId = instituicaoId