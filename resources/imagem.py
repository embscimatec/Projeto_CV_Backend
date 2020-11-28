from flask_restful import Resource, reqparse
from models.imagem import ImagemModel

class Imagem(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('encode', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('url', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('extensao', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, imagem_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Imagem.argumentos.parse_args()
        imagem = ImagemModel(**dados)

        try:
            imagem.save_imagem()
        except:
            return {'message': 'Nao foi possilvel criar essa imagem'}, 500 # Internal Server Error
        return imagem.json(), 200 # Success!
