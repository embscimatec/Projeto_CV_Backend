from sql_alchemy import banco
from models.doenca_cronica import DoencaCronicaModel

class FichaMedicaDoencaCronica(banco.Model):
    __tablename__ = 'ficha_medica_doenca_cronica'

    ficha_medica_doenca_cronica_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    
    ficha_medica_id = banco.Column(banco.Integer, banco.ForeignKey('ficha_medica.ficha_medica_id'))
    doenca_cronica_id = banco.Column(banco.Integer, banco.ForeignKey('doenca_cronica.doenca_cronica_id'))

    doenca_cronica = banco.relationship("DoencaCronicaModel", back_populates="fichas_medicas")
    ficha_medica = banco.relationship("FichaMedicaModel", back_populates="doencas_cronicas")

    def __init__(self, frequencia_uso, ficha_medica_id, doenca_cronica_id):
        self.ficha_medica_id = ficha_medica_id
        self.doenca_cronica = doenca_cronica_id

    def json(self):
        return {
            'ficha_medica_doenca_cronica_id' : self. ficha_medica_doenca_cronica_id,
            'ficha_medica_id': self.ficha_medica_id,
            'doenca_cronica_id': self.doenca_cronica_id
        }
    
    def save_ficha_medica_doenca_cronica(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_ficha_medica_doenca_cronica(self):
        banco.session.delete(self)
        banco.session.commit()

