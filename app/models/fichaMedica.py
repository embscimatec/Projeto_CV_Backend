from app import db

class FichaMedica(db.Model):
    __tablename__ = "fichaMedica"
    
    id = db.Column(db.Integer, primary_key = True)
    problemasComHemorragia = db.Column(db.bool)
    teveFilho = db.Column(db.bool)
    jaFezCirurgia = db.Column(db.bool)
    estaGravida = db.Column(db.bool)
    problemasComCicatrizacao = db.Column(db.bool)
    tipoSanguineo = db.Column(db.Enum('O+', 'O-','A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', name="enumTipoSanguineo"), nullable = False)
    deficiencia = db.Column(db.String)
    
    def __init__(self, problemasComCicatrizacao, problemasComHemorragia, teveFilho, jaFezCirurgia, estaGravida, deficiencia, tipoSanguineo):
        self.problemasComCicatrizacao = problemasComCicatrizacao
        self.problemasComHemorragia = problemasComHemorragia
        self.teveFilho = teveFilho
        self.jaFezCirurgia = jaFezCirurgia
        self.estaGravida = estaGravida
        self.deficiencia = deficiencia
        self.tipoSanguineo = tipoSanguineo