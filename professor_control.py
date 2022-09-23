from professor import Professor


class ProfessorControl:

    professores = []

    @staticmethod
    def guarda_professor(professor):
        ProfessorControl.professores.append(professor)

    @staticmethod
    def elimina_professores(codigo):
        for key, value in enumerate(ProfessorControl.professores):
            if value.codigo == codigo:
                del ProfessorControl.professores[key]
                break

    @staticmethod
    def atualiza_professores(codigo):
        for key, value in enumerate(ProfessorControl.professores):
            if value.codigo == codigo:
                pro = Professor(input("Nome Atualizado: "), input("Genero Atualizado: "),
                    input("Nivel Atualizado"), int(value.codigo))
                del ProfessorControl.professores[key]
                ProfessorControl.guarda_professor(pro)
                break

    @staticmethod
    def exibe_dados():
        for key, value in enumerate(ProfessorControl.professores):
            print(f"Nome-----------: {value.nome}")
            print(f"Genero---------: {value.genero}")
            print(f"Codigo---------: {value.codigo}")
            print(f"Nivel Academico: {value.nivel_academico}\n")
