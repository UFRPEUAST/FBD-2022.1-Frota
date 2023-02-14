class Abastecimento:
    def __init__(self, veiculo, litros, km_atual, id=None):
        self.veiculo = veiculo
        self.litros = litros.replace(',', '.')
        self.km_atual = km_atual
        self.id = id

    def __str__(self):
        return f'id: {self.id} - placa: {self.veiculo.placa} - litros: {self.litros} - ' \
               f'km {self.km_atual} '

    def get_json(self):
        return {
            'id': self.id,
            'veiculo': self.veiculo.get_json(),
            'litros': self.litros,
            'km_atual': self.km_atual,
        }
