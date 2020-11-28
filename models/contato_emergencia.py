from sql_alchemy import banco

class ContatoEmergenciaModel(banco.Model):
    __tablename__ = 'contato_emergencia'

    contato_emergencia_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(70), nullable=False)
    relacao = banco.Column(banco.String(45), nullable=False)
    email = banco.Column(banco.String(70), nullable=False)

    # Relações
    telefones = banco.relationship("TelefoneModel", backref="contato_emergencia", lazy=True)

    def __init__(self, nome, relacao, email):
        self.nome = nome
        self.relacao = relacao
        self.email = email


    def json(self):
        return {
            'contato_emergencia_id' : self.contato_emergencia_id,
            'nome': self.nome,
            'relacao': self.relacao,
            'email': self.email
        }
    
    def save_contato_emergencia(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_contato_emergencia(self):
        banco.session.delete(self)
        banco.session.commit()

