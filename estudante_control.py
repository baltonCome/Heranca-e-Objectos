from ast import Break, Pass
from estudante import Estudante


class EstudanteControl:

    estudantes = []

    @staticmethod
    def situacao(media):
        if media < 10:
            return "Excluido"
        elif 10 < media < 14:
            return "Admitido"
        else:
            return "Dispensado"

    @staticmethod
    def validacao(nota):
        if not (0 <= nota <= 20):
            print("Insira notas no intervalo de [0-20]")
            exit()

    @staticmethod
    def guarda_estudantes(estudante):
        EstudanteControl.estudantes.append(estudante)

    @staticmethod
    def elimina_estudantes(codigo):
        for key, value in enumerate(EstudanteControl.estudantes):
            if value.codigo == codigo:
                del EstudanteControl.estudantes[key]
                break

    @staticmethod
    def atualiza_estudantes(codigo):
        for key, value in enumerate(EstudanteControl.estudantes):
            if value.codigo == codigo:
                est = Estudante(input("Nome Atualizado: "), input("Genero Atualizado: "),
                                int(value.codigo), int(input("Nova nota1: ")), int(input("Nova nota2: ")))
                del EstudanteControl.estudantes[key]
                EstudanteControl.guarda_estudantes(est)
                break

    @staticmethod
    def exibe_dados():
        for key, value in enumerate(EstudanteControl.estudantes):
            print(f"Nome----: {value.nome}")
            print(f"Genero--: {value.genero}")
            print(f"Codigo--: {value.codigo}")
            print(f"Situacao: {EstudanteControl.situacao(value.media)}")
            print(f"Media---: {value.media}\n")
