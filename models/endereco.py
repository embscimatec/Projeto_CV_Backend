from sql_alchemy import banco

class EnderecoModel(banco.Model):
    __tablename__ = 'endereco'

    endereco_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    cep = banco.Column(banco.String(12), )
    logradouro = banco.Column(banco.String(70))
    numero = banco.Column(banco.String(5), nullable=False)
    bairro = banco.Column(banco.String(60))
    complemento = banco.Column(banco.String(70))
    cidade = banco.Column(banco.String(70), nullable=False)
    estado = banco.Column(banco.String(60), nullable=False)

    def __init__(self, cep, logradouro, numero, bairro, complemento, cidade, estado):
        self.cep = cep
        self.logradouro = cep
        self.numero = cep
        self.bairro = cep
        self.cep = cep
        self.cep = cep
        self.cep = cep


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

