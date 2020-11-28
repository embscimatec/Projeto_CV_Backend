from flask_restful import Resource, reqparse
from models.pessoa import PessoaModel

class Pessoa(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('sobrenome', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('sexo', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('cpf', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('email', type=str, required=False)
    argumentos.add_argument('data_de_nascimento', type=str, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('tem_gemeo', type=str, required=True, help="Este campo não pode ficar vazio")

    def get(self, pessoa_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = Pessoa.argumentos.parse_args()
        pessoa = PessoaModel(**dados)

        try:
            pessoa.save_pessoa()
        except:
            return {'message': 'Nao foi possilvel registrar essa pessoa'}, 500 # Internal Server Error
        return pessoa.json(), 200 # Success!
