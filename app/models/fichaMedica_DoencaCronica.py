from app import db
from sqlalchemy.orm import relationship

class FichaMedicaDoencaCronica(db.Model)
    id = db.Column(db.Integer, primary_key = True)

    __tablename__ = 'fichaMedicaDoencaCronica'
    fichaMedicaId= db.Column(Integer, ForeignKey('fichaMedica.id'), primary_key = True)
    doencaCronicaId = db.Column(Integer, ForeignKey('doencaCronica.id'), primary_key = True)
    familiar = db.Column(db.bool)
    pessoa = db.Column(db.bool)
    fichaMedica = relationship("FichaMedica", back_populates="doencasCronicas")
    doencaCronica = relationship("DoencaCronica", back_populates="fichaMedicas")

    def __init__(self, fichaMedicaId, doencaCronicaId, familiar, pessoa, fichaMedica, doencaCronica):
        self.fichaMedicaId = fichaMedicaId
        self.doencaCronicaId = doencaCronicaId
        self.familiar = familiar
        self.pessoa = pessoa
        self.fichaMedica = fichaMedica
        self.doencaCronica = doencaCronica

