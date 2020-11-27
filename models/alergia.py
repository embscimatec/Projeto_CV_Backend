from sql_alchemy import banco


class AlergiaModel(banco.Model):
    __tablename__ = 'alergia'

    alergia_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    substancia = banco.Column(banco.String(60))


    def __init__(self, substancia):
        self.substancia = substancia

    def json(self):
        return {
            'alergia_id' : self.alergia_id,
            'substancia': self.substancia
        }
    
    def save_alergia(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_alergia(self):
        banco.session.delete(self)
        banco.session.commit()

