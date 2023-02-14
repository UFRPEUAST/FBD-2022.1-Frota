from flask import Flask, make_response, jsonify, request, Response
from database.connect import ConnectDataBase
from modulos.abastecimento.dao import DaoAbastecimento
from modulos.abastecimento.modelo import Abastecimento
from modulos.veiculo.dao import DaoVeiculo
from modulos.veiculo.modelo import Veiculo

app = Flask(__name__)
ConnectDataBase().init_table()

dao_veiculo = DaoVeiculo()
dao_abastecimento = DaoAbastecimento()


@app.route('/veiculos/', methods=['GET'])
def veiculos():
    parametros = request.args
    busca = parametros.get('busca', None)
    veiculos = dao_veiculo.get_veiculos(busca)
    return make_response(jsonify(veiculos))


@app.route('/veiculo/add/', methods=['POST'])
def add_veiculo():
    data_veiculo = dict(request.form)
    veiculo = Veiculo(**data_veiculo)
    id = dao_veiculo.salvar(veiculo)
    veiculo.id = id
    return make_response({})


@app.route('/veiculo/<int:id>/', methods=['GET'])
def veiculo_id(id: int):
    veiculo = dao_veiculo.get_por_id(id)
    if not veiculo:
        return Response({}, status=404)
    return make_response(jsonify(veiculo.get_json()))


@app.route('/veiculo/<int:id>/', methods=['PUT'])
def atualizar_veiculo(id: int):
    data_veiculo = dict(request.form)
    veiculo = dao_veiculo.get_por_id(id)
    veiculo.placa = data_veiculo.get('placa')
    veiculo.modelo = data_veiculo.get('modelo')
    if dao_veiculo.atualizar(veiculo):
        return make_response(jsonify(veiculo.get_json()))
    return Response({}, status=404)


@app.route('/veiculo/<int:id>/abastecimento/add/', methods=['POST'])
def add_abastecimento(id: int):
    veiculo = dao_veiculo.get_por_id(id)
    if not veiculo:
        return Response({}, status=404)
    data_abastecimento = dict(request.form)
    abastecimento = Abastecimento(veiculo=veiculo, **data_abastecimento)
    id = dao_abastecimento.salvar(abastecimento)
    abastecimento.id = id
    return make_response(jsonify(abastecimento.get_json()))


@app.route('/veiculo/<int:id>/abastecimentos/', methods=['GET'])
def veiculos_abastecimentos(id: int):
    veiculo = dao_veiculo.get_por_id(id)
    if not veiculo:
        return Response({}, status=404)
    abastecimentos = dao_abastecimento.get_por_veiculo(veiculo.id)
    return make_response(jsonify(abastecimentos))

app.run()
