from sql_alchemy import banco


class MedicamentoModel(banco.Model):
    __tablename__ = 'medicamento'

    medicamento_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    nome = banco.Column(banco.String(60))


    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'medicamento_id' : self.medicamento_id,
            'nome': self.nome
        }
    
    def save_medicamento(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_medicamento(self):
        banco.session.delete(self)
        banco.session.commit()

