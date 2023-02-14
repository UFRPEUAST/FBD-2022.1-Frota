class SQLVeiculo:
    _NOME_TABELA = 'veiculo'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'placa varchar(8) unique,' \
                           f'modelo varchar(8))'
    _SCRIPT_INSET = f'INSERT INTO {_NOME_TABELA}(placa,modelo) ' \
                    f'values(%s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _SELECT_BUSCA = "SELECT * FROM {} where placa ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET placa=%s, modelo=%s ' \
                    f'WHERE id=%s'