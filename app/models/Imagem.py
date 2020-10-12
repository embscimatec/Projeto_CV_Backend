from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from app import db

class Imagem(db.Model):
    __tablename__ = "imagem"
    
    imagemId = db.Column(db.Integer, primary_key = True)
    encode = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    extensao = db.Column(db.String(10), nullable = False)
    pessoa = db.relationship("Pessoa", uselist = False, back_populates = "imagem")
    
    def __init__(self, encode, url, extensao):
        self.encode = encode
        self.url = url
        self.extensao = extensao