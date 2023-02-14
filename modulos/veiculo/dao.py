from flask import Response

from database.connect import ConnectDataBase
from modulos.veiculo.modelo import Veiculo
from modulos.veiculo.sql import SQLVeiculo


class DaoVeiculo():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_veiculos(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLVeiculo._SELECT_BUSCA.format(SQLVeiculo._NOME_TABELA,
                                              busca) if busca else SQLVeiculo._SELECT_ALL

        cursor.execute(sql)
        veiculos = []
        coluns_name = [desc[0] for desc in cursor.description]
        for veiculo in cursor.fetchall():
            data = dict(zip(coluns_name, veiculo))
            veiculos.append(Veiculo(**data).get_json())
        return veiculos

    def salvar(self, veiculo):
        cursor = self.connect.cursor()
        cursor.execute(SQLVeiculo._SCRIPT_INSET,
                       (veiculo.placa, veiculo.modelo)
                       )
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_por_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLVeiculo._SELECT_ID, (str(id)))
        veiculo = cursor.fetchone()
        if not veiculo:
            return None
        coluns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(coluns_name, veiculo))
        return Veiculo(**data)

    def atualizar(self, veiculo):
        cursor = self.connect.cursor()
        cursor.execute(SQLVeiculo._UPDATE_BY_ID, (veiculo.placa, veiculo.modelo, veiculo.id))
        self.connect.commit()
        return True