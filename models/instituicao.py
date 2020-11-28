from sql_alchemy import banco

class InstituicaoModel(banco.Model):
    __tablename__ = 'instituicao'

    instituicao_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(70), nullable=False)
    email = banco.Column(banco.String(70), nullable=False)
    senha = banco.Column(banco.String(45), nullable=False)
    pessoas = banco.relationship("PessoaModel", backref="instituicao", lazy=True)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def json(self):
        return {
            'instituicao_id' : self.instituicao_id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }
    
    def save_instituicao(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_instituicao(self):
        banco.session.delete(self)
        banco.session.commit()

