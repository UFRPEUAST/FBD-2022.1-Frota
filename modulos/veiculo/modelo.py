class Veiculo(object):
    def __init__(self, placa, modelo, id=None):
        self.placa = placa
        self.modelo = modelo
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - PLaca: {self.placa} - Modelo{self.modelo}'

    def get_json(self):
        return {
            'id': self.id,
            'placa': self.placa,
            'modelo': self.modelo,
        }

    def get_sql_insert(self):
        return
