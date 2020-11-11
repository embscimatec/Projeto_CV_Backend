from flask_restful import Resource, reqparse
from models.sintoma import SintomaModel

class Sintoma(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be empty")


    def get(self, sintoma_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Sintoma.argumentos.parse_args()
        sintoma = SintomaModel(**dados)

        try:
            sintoma.save_sintoma()
        except:
            return {'message': 'An error occurred while saving the hotel'}, 500 # Internal Server Error
        return sintoma.json(), 200 # Success!
