import psycopg2

from modulos.veiculo.sql import SQLVeiculo


class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="fbd_frota",
            user="postgres",
            password="postgres"
        )

    def get_instance(self):
        return self._connect

    def init_table(self):
        cursor = self._connect.cursor()
        cursor.execute(SQLVeiculo._SCRIPT_CREATE_TABLE)
        self._connect.commit()
    def sql_new(self):
        return