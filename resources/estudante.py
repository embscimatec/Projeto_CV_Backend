from flask_restful import Resource, reqparse
from models.estudante import EstudanteModel

class Estudante(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('matricula', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, estudante_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Estudante.argumentos.parse_args()
        estudante = EstudanteModel(**dados)

        try:
            estudante.save_estudante()
        except:
            return {'message': 'Nao foi possilvel criar esse estudante'}, 500 # Internal Server Error
        return estudante.json(), 200 # Success!
