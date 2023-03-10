class SQLAbastecimento:
    _NOME_TABELA = 'abastecimento'
    _TABLE_VEICULO = 'veiculo'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'km_atual int,' \
                           f'litros decimal,' \
                           f'veiculo_id int  references veiculo(id))'
    _SCRIPT_INSET = f'INSERT INTO {_NOME_TABELA}(veiculo_id,litros, km_atual) ' \
                    f'values(%s, %s, %s) RETURNING id'
    _SELECT_BY_VEICULO_ID = f'SELECT km_atual, litros FROM {_NOME_TABELA} WHERE veiculo_id=%s'
    _SELECT_ALL_AND_VEICULO = (f'select ab.km_atual, ab.litros, ve.modelo, ve.placa from {_NOME_TABELA} as ab '
                               f'inner join {_TABLE_VEICULO} as ve on ab.veiculo_id = ve.id;')
    # _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    # _SELECT_BUSCA = "SELECT * FROM {} where placa ILIKE '%{}%'"
    #
    # _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET placa=%s, modelo=%s ' \
    #                 f'WHERE id=%s'
