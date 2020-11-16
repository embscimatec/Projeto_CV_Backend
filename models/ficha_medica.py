from sql_alchemy import banco
from models.ficha_medica_droga import FichaMedicaDrogaModel

class FichaMedicaModel(banco.Model):
    __tablename__ = 'ficha_medica'

    ficha_medica_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    problemas_cicatrizacao = banco.Column(banco.Boolean)
    teve_filho = banco.Column(banco.Boolean)
    ja_fez_cirurgia = banco.Column(banco.Boolean)
    esta_gravida = banco.Column(banco.Boolean)
    problemas_hemorragia = banco.Column(banco.Boolean)
    tipo_sanguineo = banco.Column(banco.Enum("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"))
    drogas = banco.relationship("FichaMedicaDrogaModel", back_populates="ficha_medica")

    def __init__(self, problemas_cicatrizacao, teve_filho, ja_fez_cirurgia, esta_gravida, problemas_hemorragia, tipo_sanguineo):
        self.problemas_cicatrizacao = problemas_cicatrizacao
        self.teve_filho = teve_filho
        self.ja_fez_cirurgia = ja_fez_cirurgia
        self.esta_gravida = esta_gravida
        self.problemas_hemorragia = problemas_hemorragia
        self.tipo_sanguineo = tipo_sanguineo

    def json(self):
        return {
            'ficha_medica_id' : self.ficha_medica_id,
            'problemas_cicatrizacao': self.problemas_cicatrizacao,
            'teve_filho': self.teve_filho,
            'ja_fez_cirurgia': self.ja_fez_cirurgia,
            'esta_gravida': self.esta_gravida,
            'problemas_hemorragia': self.problemas_hemorragia,
            'tipo_sanguineo': self.tipo_sanguineo
        }
    
    def save_ficha_medica(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_ficha_medica(self):
        banco.session.delete(self)
        banco.session.commit()

