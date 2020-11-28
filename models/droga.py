from sql_alchemy import banco
from models.ficha_medica_droga import FichaMedicaDrogaModel

class DrogaModel(banco.Model):
    __tablename__ = 'droga'

    droga_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(60))
    fichas_medicas = banco.relationship("FichaMedicaDrogaModel", back_populates="droga")

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'droga_id' : self.droga_id,
            'nome': self.nome
        }
    
    def save_droga(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_droga(self):
        banco.session.delete(self)
        banco.session.commit()

