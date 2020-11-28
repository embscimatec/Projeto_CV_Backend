from sql_alchemy import banco

class TelefoneModel(banco.Model):
    __tablename__ = 'telefone'

    telefone_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    DDI = banco.Column(banco.String(3), nullable=False)
    DDD = banco.Column(banco.String(3), nullable=False)
    numero = banco.Column(banco.String(9), nullable=False)

    # Relações
    pessoa_id = banco.Column(banco.Integer, banco.ForeignKey('pessoa.pessoa_id'), nullable=False)

    def __init__(self, DDI, DDD, numero):
        self.DDI = DDI
        self.DDD = DDD
        self.numero = numero


    def json(self):
        return {
            'telefone_id' : self.telefone_id,
            'DDI': self.DDI,
            'DDD': self.DDD,
            'numero': self.numero
        }
    
    def save_telefone(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_telefone(self):
        banco.session.delete(self)
        banco.session.commit()

