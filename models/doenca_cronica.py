from sql_alchemy import banco
#from models.doenca_cronica_sintoma import DoencaCronicaSintomaModel

class DoencaCronicaModel(banco.Model):
    __tablename__ = 'doenca_cronica'

    doenca_cronica_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(60))
    sintomas = banco.relationship("DoencaCronicaSintomaModel", back_populates="doenca_cronica")
    

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'doenca_cronica_id' : self.doenca_cronica_id,
            'nome': self.nome
        }
    
    def save_doenca_cronica(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_doenca_cronica(self):
        banco.session.delete(self)
        banco.session.commit()
