from pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome, genero, nivel_academico, codigo):
        super().__init__(nome, genero)
        self._nivel_academico = nivel_academico
        self._codigo = codigo

    @property
    def nivel_academico(self):
        return self._nivel_academico

    @nivel_academico.setter
    def nivel_academico(self, nivel_academico):
        self._nivel_academico = nivel_academico

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

