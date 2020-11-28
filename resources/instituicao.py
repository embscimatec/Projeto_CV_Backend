from flask_restful import Resource, reqparse
from models.instituicao import InstituicaoModel

class Instituicao(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('email', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('senha', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, instituicao_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Instituicao.argumentos.parse_args()
        instituicao = InstituicaoModel(**dados)

        try:
            instituicao.save_instituicao()
        except:
            return {'message': 'Nao foi possilvel criar essa instituicao'}, 500 # Internal Server Error
        return instituicao.json(), 200 # Success!
