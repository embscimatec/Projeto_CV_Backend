from sql_alchemy import banco

class EnderecoModel(banco.Model):
    __tablename__ = 'endereco'

    endereco_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    cep = banco.Column(banco.String(12))
    logradouro = banco.Column(banco.String(70))
    numero = banco.Column(banco.String(5), nullable=False)
    bairro = banco.Column(banco.String(60))
    complemento = banco.Column(banco.String(70))
    cidade = banco.Column(banco.String(70), nullable=False)
    estado = banco.Column(banco.String(60), nullable=False)
    pessoas = banco.relationship("PessoaModel", backref="endereco", lazy=True)

    def __init__(self, cep, logradouro, numero, bairro, complemento, cidade, estado):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado


    def json(self):
        return {
            'endereco_id' : self.endereco_id,
            'cep': self.cep,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'complemento': self.complemento,
            'cidade': self.cidade,
            'estado': self.estado
        }
    
    def save_endereco(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_endereco(self):
        banco.session.delete(self)
        banco.session.commit()

