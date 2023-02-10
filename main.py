# from modulos.curso.curso import Curso
# from modulos.curso.dao import CursoDao
#
# # curso = Curso(nome='Eng. de Pesca',
# #               sigla='eng_pesca')
# dao_curso = CursoDao()
# # curso = dao_curso.salvar(curso)
#
# cursos = dao_curso.get_all()
# for c in cursos:
#     print(c)
#
# print('**')
# curso = dao_curso.get_por_id(6)
# print(curso)


def teste(nome, cpf):
    print('nome', nome)
    print('cpf', cpf)


data = {
    'nome': 'HELDON',
    'cpf': '050'
}
lista = ['122', '123']
teste(*data)
