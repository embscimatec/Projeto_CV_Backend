from flask_restful import Resource, reqparse
from models.endereco import EnderecoModel

class Endereco(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('CEP', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('logradouro', type=str, required=False)
    argumentos.add_argument('numero', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('bairro', type=str, required=False)
    argumentos.add_argument('complemento', type=str, required=False)
    argumentos.add_argument('cidade', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('estado', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, endereco_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Endereco.argumentos.parse_args()
        endereco = EnderecoModel(**dados)

        try:
            endereco.save_endereco()
        except:
            return {'message': 'Nao foi possilvel salvar endereco'}, 500 # Internal Server Error
        return endereco.json(), 200 # Success!
