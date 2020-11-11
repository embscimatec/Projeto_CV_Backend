from sql_alchemy import banco

class SintomaModel(banco.Model):
    __tablename__ = 'sintomas'

    sintoma_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(60))

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'sintoma_id' : self.sintoma_id,
            'nome': self.nome
        }
    
    def save_sintoma(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_sintoma(self):
        banco.session.delete(self)
        banco.session.commit()

