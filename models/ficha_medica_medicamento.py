from sql_alchemy import banco
from models.medicamento import MedicamentoModel

class FichaMedicaMedicamentoModel(banco.Model):
    __tablename__ = 'ficha_medica_medicamento'

    ficha_medica_medicamento_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    dose = banco.Column(banco.String(15))
    tipo =  banco.Column(banco.Enum("comprimido", "gotas", "pastilha"))
    intervalo_uso = banco.Column(banco.DateTime)
    
    ficha_medica_id = banco.Column(banco.Integer, banco.ForeignKey('ficha_medica.ficha_medica_id'))
    medicamento_id = banco.Column(banco.Integer, banco.ForeignKey('medicamento.medicamento_id'))

    medicamento = banco.relationship("MedicamentoModel")
    ficha_medica = banco.relationship("FichaMedicaModel", back_populates="medicamentos")

    def __init__(self, dose, tipo, intervalo_uso, ficha_medica_id, medicamento_id):
        self.dose= dose
        self.tipo = tipo
        self.intervalo_uso = intervalo_uso
        self.ficha_medica_id = ficha_medica_id
        self.medicamento_id = medicamento_id

    def json(self):
        return {
            'ficha_medica_medicamento_id' : self. ficha_medica_droga_id,
            'dose': self.dose,
            'tipo': self.tipo,
            'intervalo_uso': self.intervalo_uso,
            'ficha_medica_id': self.ficha_medica_id,
            'medicamento_id': self.medicamento_id
        }
    
    def save_ficha_medica_medicamento(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_ficha_medica_medicamento(self):
        banco.session.delete(self)
        banco.session.commit()

