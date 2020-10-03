from app import db

class Sintoma(db.Model):
    __tablename__ = "sintoma"
    
    id = db.Column(db.Integer, primary_key = True)
    nomeSintoma = db.Column(db.String)
    
    def __init__(self, nomeSintoma):
        self.nomeSintoma = nomeSintoma
    