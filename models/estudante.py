from sql_alchemy import banco

class EstudanteModel(banco.Model):
    __tablename__ = 'estudante'

    estudante_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    matricula = banco.Column(banco.String(50), nullable=False)

    contato_emergencia_id = banco.Column(banco.Integer, banco.ForeignKey('contato_emergencia.contato_emergencia_id'), nullable=False)
    pessoa_id = banco.Column(banco.Integer, banco.ForeignKey('pessoa.pessoa_id'), nullable=False)
    #Todo ficha médica relação

    def __init__(self, matricula):
        self.matricula = matricula


    def json(self):
        return {
            'estudante' : self.estudante_id,
            'matricula': self.matricula
            #TODO pessoa_id, ficha médica...
        }
    
    def save_estudante(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_estudante(self):
        banco.session.delete(self)
        banco.session.commit()

