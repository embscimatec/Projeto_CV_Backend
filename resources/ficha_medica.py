from flask_restful import Resource, reqparse
from models.ficha_medica import FichaMedicaModel

class FichaMedica(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('problemas_cicatrizacao', type= bool, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('teve_filho', type= bool, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('ja_fez_cirurgia', type= bool, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('esta_gravida', type= bool, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('problemas_hemorragia', type= bool, required=True, help="Este campo não pode ficar vazio")
    argumentos.add_argument('tipo_sanguineo', type= str, required=True, help="Este campo não pode ficar vazio")

    def get(self, ficha_medica_id):
        # TODO: Adicionar classmethod para procurar pelo ID
        return None

    def post(self):
        dados = FichaMedica.argumentos.parse_args()
        fichaMedica = FichaMedicaModel(**dados)

        try:
            fichaMedica.save_ficha_medica()
        except:
            return {'message': 'Nao foi possilvel salvar essa ficha'}, 500 # Internal Server Error
        return fichaMedica.json(), 200 # Success!
