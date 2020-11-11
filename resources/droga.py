from flask_restful import Resource, reqparse
from models.droga import DrogaModel

class Droga(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be empty")


    def get(self, sintoma_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Droga.argumentos.parse_args()
        droga = DrogaModel(**dados)

        try:
            droga.save_droga()
        except:
            return {'message': 'An error occurred while saving drugs'}, 500 # Internal Server Error
        return droga.json(), 200 # Success!
