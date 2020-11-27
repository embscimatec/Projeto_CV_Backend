from sql_alchemy import banco
from models.alergia import AlergiaModel

class FichaMedicaAlergiaModel(banco.Model):
    __tablename__ = 'ficha_medica_alergia'

    ficha_medica_alergia_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    grau = banco.Column(banco.Enum("muito alérgico", "pouco alérgico", "alérgico"))
    
    ficha_medica_id = banco.Column(banco.Integer, banco.ForeignKey('ficha_medica.ficha_medica_id'))
    alergia_id = banco.Column(banco.Integer, banco.ForeignKey('alergia.alergia_id'))

    alergia = banco.relationship("AlergiaModel")
    ficha_medica = banco.relationship("FichaMedicaModel", back_populates="alergias")

    def __init__(self, grau, ficha_medica_id, alergia_id):
        self.grau = grau
        self.ficha_medica_id = ficha_medica_id
        self.alergia_id = alergia_id

    def json(self):
        return {
            'ficha_medica_alergia_id' : self. ficha_medica_alergia_id,
            'grau': self.grau,
            'ficha_medica_id': self.ficha_medica_id,
            'alergia_id': self.alergia_id
        }
    
    def save_ficha_medica_alergia(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_ficha_medica_alergia(self):
        banco.session.delete(self)
        banco.session.commit()

