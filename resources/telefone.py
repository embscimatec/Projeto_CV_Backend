from flask_restful import Resource, reqparse
from models.telefone import TelefoneModel

class Telefone(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('DDI', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('DDD', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('numero', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, telefone_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Telefone.argumentos.parse_args()
        telefone = TelefoneModel(**dados)

        try:
            telefone.save_telefone()
        except:
            return {'message': 'Nao foi possilvel criar esse telefone'}, 500 # Internal Server Error
        return telefone.json(), 200 # Success!
