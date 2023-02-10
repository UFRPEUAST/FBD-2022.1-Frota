from flask import Flask, make_response, jsonify, request, Response
from database.connect import ConnectDataBase
from modulos.veiculo.dao import DaoVeiculo

app = Flask(__name__)
ConnectDataBase().init_table()

dao_veiculo = DaoVeiculo()


@app.route('/veiculos/', methods=['GET'])
def veiculos():
    parametros = request.args
    busca = parametros.get('busca', None)
    veiculos = dao_veiculo.get_veiculos(busca)
    return make_response(jsonify(veiculos))


@app.route('/veiculo/<int:id>/', methods=['GET'])
def veiculo_id(id: int):
    veiculo = dao_veiculo.get_por_id(id)
    if not veiculo:
        return Response({}, status=404)
    return make_response(jsonify(veiculo.get_json()))


app.run()
