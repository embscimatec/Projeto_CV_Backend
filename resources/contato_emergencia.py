from flask_restful import Resource, reqparse
from models.contato_emergencia import ContatoEmergenciaModel

class ContatoEmergencia(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('relacao', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('email', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, contato_emergencia_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = ContatoEmergencia.argumentos.parse_args()
        contato_emergencia = ContatoEmergenciaModel(**dados)

        try:
            contato_emergencia.save_contato_emergencia()
        except:
            return {'message': 'Nao foi possivel criar esse contato de emergencia'}, 500 # Internal Server Error
        return contato_emergencia.json(), 200 # Success!
