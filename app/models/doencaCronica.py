from app import db

class DoencaCronica(db.Model):
    __tablename__ = "doencaCronica"
    
    id = db.Column(db.Integer, primary_key = True)
    nomeDencaCronica = db.Column(db.String)
    
    def __init__(self, nomeDencaCronica):
        self.nomeDencaCronica = nomeDencaCronica
    