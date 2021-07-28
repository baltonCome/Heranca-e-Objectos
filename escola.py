from professor import Professor
from estudante import Estudante
from estudante_control import EstudanteControl as Estu
from professor_control import ProfessorControl as Prof


class Main:
    escola = True
    codigo_professor = 0
    codigo_estudante = 0

    while escola:
        escolha = int(input("[1}Estudantes\n[2]Professores\n[0]Sair\n>>>>>>>"))
        if escolha == 1:
            escolha2 = int(input("[1]Registo\n[2]Visualizar Registados\n[3]Atualizar Dados\n[4]Remover\n>>>>>>>>"))
            if escolha2 == 1:
                codigo_estudante += 1
                estudante = Estudante(input("Nome: "), input("Genero: "), codigo_estudante,
                                      float(input("Nota1: ")), float(input("Nota2: ")))
                Estu.guarda_estudantes(estudante)
            elif escolha2 == 2:
                Estu.exibe_dados()
            elif escolha2 == 3:
                Estu.atualiza_estudantes(int(input("Numero do estudante a atualizar: ")))
            elif escolha2 == 4:
                Estu.elimina_estudantes(int(input("Numero do estudante a eliminar: ")))
        elif escolha == 2:
            escolha3 = int(input("[1]Registo\n[2]Visualizar Registados\n[3]Atualizar Dados\n[4]Remover\n>>>>>>>>"))
            if escolha3 == 1:
                codigo_professor += 1
                professor = Professor(input("Nome: "), input("Genero: "), input("Nivel Academico: "), codigo_professor)
                Prof.guarda_professor(professor)
            elif escolha3 == 2:
                Prof.exibe_dados()
            elif escolha3 == 3:
                Prof.atualiza_professores(int(input("Codigo do professor a atualizar: ")))
            elif escolha3 == 4:
                Prof.elimina_professores(int(input("Codigo do professor a eliminar: ")))
        elif escolha == 0:
            escola = False
