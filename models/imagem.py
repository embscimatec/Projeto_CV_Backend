from sql_alchemy import banco

class ImagemModel(banco.Model):
    __tablename__ = 'imagem'

    imagem_id = banco.Column(banco.Integer, primary_key=True) #autoincrement
    encode = banco.Column(banco.String(500), nullable=False)
    url = banco.Column(banco.String(100), nullable=False)
    extensao = banco.Column(banco.String(4), nullable=False)
    pessoa_id = banco.Column(banco.Integer, banco.ForeignKey('pessoa.pessoa_id'), nullable=False)

    def __init__(self, encode, url, extensao):
        self.encode = encode
        self.url = url
        self.extensao = extensao


    def json(self):
        return {
            'imagem_id' : self.imagem_id,
            'encode': self.encode,
            'url': self.url,
            'extensao': self.extensao
            #TODO pessoa_id
        }
    
    def save_imagem(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_imagem(self):
        banco.session.delete(self)
        banco.session.commit()

