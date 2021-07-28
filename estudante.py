from pessoa import Pessoa


class Estudante(Pessoa):

    def __init__(self, nome, genero, codigo, nota1, nota2):
        super().__init__(nome, genero)
        self._codigo = codigo
        self._nota1 = nota1
        self._nota2 = nota2

    @property
    def codigo(self):
        return self._codigo

    @property
    def nota1(self):
        return self._nota1

    @property
    def nota2(self):
        return self._nota2

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @nota1.setter
    def nota1(self, nota1):
        self._nota1 = nota1

    @nota2.setter
    def nota2(self, nota2):
        self._nota2 = nota2

    @property
    def media(self):
        return (self._nota1 + self._nota2)/2
