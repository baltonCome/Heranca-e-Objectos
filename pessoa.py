import abc


class Pessoa(abc.ABC):

    def __init__(self, nome, genero):
        self._nome = nome
        self._genero = genero

    @property
    def nome(self):
        return self._nome

    @property
    def genero(self):
        return self._genero

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @genero.setter
    def genero(self, genero):
        self._genero = genero
