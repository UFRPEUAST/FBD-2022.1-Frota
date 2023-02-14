from database.connect import ConnectDataBase
from modulos.abastecimento.sql import SQLAbastecimento


class DaoAbastecimento():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar(self, abastecimento):
        veiculo = abastecimento.veiculo
        cursor = self.connect.cursor()
        cursor.execute(SQLAbastecimento._SCRIPT_INSET,
                       (veiculo.id, abastecimento.litros,
                        abastecimento.km_atual))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_por_veiculo(self, id_veiculo):
        cursor = self.connect.cursor()
        sql = SQLAbastecimento._SELECT_BY_VEICULO_ID

        cursor.execute(sql, (str(id_veiculo)))
        abastecimentos = []
        coluns_name = [desc[0] for desc in cursor.description]
        for veiculo in cursor.fetchall():
            data = dict(zip(coluns_name, veiculo))
            abastecimentos.append(data)
            # print('data', data)
            # veiculos.append(Veiculo(**data).get_json())
        return abastecimentos
