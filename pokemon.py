import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return f'{self.especie} (LV {self.level})'

    def atacar(self, pokemon):
        print(f'{self} atacou {pokemon}')


class pokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print(f'{self} lançou RAIO DO TROVÃO em {pokemon}')


class pokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print(f'{self} lançou BOLA DE FOGO em {pokemon}')


class pokemonAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print(f'{self} lançou JATO DE AGUA em {pokemon}')