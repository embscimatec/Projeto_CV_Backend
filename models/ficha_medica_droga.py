from sql_alchemy import banco
#from models.droga import DrogaModel
#from models.ficha_medica import FichaMedicaModel

class FichaMedicaDrogaModel(banco.Model):
    __tablename__ = 'ficha_medica_droga'

    ficha_medica_droga_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    frequencia_uso = banco.Column(banco.Enum("nunca", "até uma vez por mês", "duas a quatro vezes por mês", " duas a três vezes por semana", "quatro ou mais vezes por semana"))
    
    ficha_medica_id = banco.Column(banco.Integer, banco.ForeignKey('ficha_medica.ficha_medica_id'))
    droga_id = banco.Column(banco.Integer, banco.ForeignKey('droga.droga_id'))

    droga = banco.relationship("DrogaModel", back_populates="fichas_medicas")
    ficha_medica = banco.relationship("FichaMedicaModel", back_populates="drogas")

    def __init__(self, frequencia_uso, ficha_medica_id, droga_id):
        self.frequencia_uso = frequencia_uso
        self.ficha_medica_id = ficha_medica_id
        self.droga_id = droga_id

    def json(self):
        return {
            'ficha_medica_droga_id' : self. ficha_medica_droga_id,
            'frequencia_uso': self.frequencia_uso,
            'ficha_medica_id': self.ficha_medica_id,
            'droga_id': self.droga_id
        }
    
    def save_ficha_medica_droga(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_ficha_medica_droga(self):
        banco.session.delete(self)
        banco.session.commit()

