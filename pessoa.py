import random

from pokemon import *


NOMES = [
        "João", "Maria", "Pedro", "Ana", "Luiz",
        "Sofia", "Miguel", "Lara", "Carlos", "Beatriz",
        "Gustavo", "Isabella", "Fernando", "Camila", "Rafael",
        "Gary",
]


POKEMONS = [
    pokemonAgua("Squirtle"),
    pokemonAgua("Vaporeon"),
    pokemonAgua("Blastoise"),
    pokemonFogo("Charmander"),
    pokemonFogo("Ninetales"),
    pokemonFogo("Arcanine"),
    pokemonEletrico("Pikachu"),
    pokemonEletrico("Raichu"),
    pokemonEletrico("Jolteon"),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}')
            for i, pokemon in enumerate(self.pokemons):
                print(f'{i} - {pokemon}')
        else:
            print(f'{self} não tem pokemons')


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido} para a batalha! ')
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não possui Pokemons!')


    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon_player = self.escolher_pokemon()

        if pokemon_player and pokemon_inimigo:
            while True:
                vitoria = pokemon_player.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha!')
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon_player)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha!')
                    break
        else:
            print('Essa batalha não pode ocorrer')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('Escolha seu Pokemon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} EU ESCOLHO VOCÊ!!! ')
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('ERRO: Esse jogador não possui Pokemons!')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=None, pokemons=pokemons)




