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

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f'{self.especie} (LV {self.level})'

    def atacar(self, pokemon):
        pokemon.vida = pokemon.vida - pokemon.ataque
        print(f'{pokemon} perdeu {self.ataque} pontos de vida')

        if pokemon.vida <= 0:
            print(f'{pokemon} foi derrotado!')
            return True
        else:
            return False


class pokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print(f'{self} lançou RAIO DO TROVÃO em {pokemon}')
        return super().atacar(pokemon)


class pokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print(f'{self} lançou BOLA DE FOGO em {pokemon}')
        return super().atacar(pokemon)


class pokemonAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print(f'{self} lançou JATO DE AGUA em {pokemon}')
        return super().atacar(pokemon)