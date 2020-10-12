from app import db
from sqlalchemy.orm import relationship

class DoencaCronicaSintoma(db.Model)
    id = db.Column(db.Integer, primary_key = True)

    __tablename__ = 'doencaCronicaSintoma'
    sintomaId= db.Column(Integer, ForeignKey('sintoma.id'), primary_key = True)
    doencaCronicaId = db.Column(Integer, ForeignKey('doencaCronica.id'), primary_key = True)
    sintoma  = relationship("Sintoma", back_populates="doencasCronicas")
    doencaCronica = relationship("DoencaCronica", back_populates="sintomas")

    def __init__(self, sintomaId, sintoma,doencaCronicaId, doencaCronica):
        self.doencaCronicaId = doencaCronicaId
        self.doencaCronica = doencaCronica
        self.sintoma = sintoma
        self.sintomaId = sintomaId
