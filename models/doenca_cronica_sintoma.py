from sql_alchemy import banco
from models.doenca_cronica import DoencaCronicaModel
from models.sintoma import SintomaModel


class DoencaCronicaSintomaModel(banco.Model):
    __tablename__ = 'doenca_cronica_sintoma'

    doenca_cronica_sintoma_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    
    doenca_cronica_id = banco.Column(banco.Integer, banco.ForeignKey('doenca_cronica.doenca_cronica_id'))
    sintoma_id = banco.Column(banco.Integer, banco.ForeignKey('sintoma.sintoma_id'))

    sintoma = banco.relationship("SintomaModel", back_populates="doencas_cronicas")
    doenca_cronica = banco.relationship("DoencaCronicaModel", back_populates="sintomas")

    def __init__(self, doenca_cronica_id, sintoma_id):
        self.doenca_cronica_id = doenca_cronica_id
        self.sintoma_id = sintoma_id

    def json(self):
        return {
            'doenca_cronica_sintoma_id' : self. doenca_cronica_sintoma_id,
            'doenca_cronica_id': self.doenca_cronica_id,
            'sintoma_id': self.sintoma_id
        }
    
    def save_doenca_cronica_sintoma(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_doenca_cronica_sintoma(self):
        banco.session.delete(self)
        banco.session.commit()

