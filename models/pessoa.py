from sql_alchemy import banco

class PessoaModel(banco.Model):
    __tablename__ = 'pessoa'

    pessoa_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(35), nullable=False)
    sobrenome = banco.Column(banco.String(65), nullable=False)
    sexo = banco.Column(banco.Enum('M', 'F', 'I'), nullable=False)
    cpf = banco.Column(banco.String(15), nullable=False)
    email = banco.Column(banco.String(70), nullable=True)
    data_de_nascimento = banco.Column(banco.DateTime, nullable=False)
    tem_gemeo = banco.Column(banco.Bool, nullable=False)

    # Relações
    instituicao_id = banco.Column(banco.Integer, banco.ForeignKey('instituicao.instituicao_id'), nullable=False)
    endereco_id = banco.Column(banco.Integer, banco.ForeignKey('endereco.endereco_id'), nullable=False)

    def __init__(self, nome, sobrenome, sexo, cpf, email, data_de_nascimento, tem_gemeo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf
        self.email = email
        self.data_de_nascimento = data_de_nascimento
        self.tem_gemeo = tem_gemeo


    def json(self):
        return {
            'pessoa_id' : self.pessoa_id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'sexo': self.sexo,
            'cpf': self.cpf,
            'email': self.email,
            'data_de_nascimento': self.data_de_nascimento,
            'tem_gemeo': self.tem_gemeo
        }
    
    def save_pessoa(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_pessoa(self):
        banco.session.delete(self)
        banco.session.commit()

