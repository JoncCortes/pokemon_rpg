import random

from pokemon import *


NOMES = [
        "João", "Maria", "Pedro", "Ana", "Luiz",
        "Sofia", "Miguel", "Lara", "Carlos", "Beatriz",
        "Gustavo", "Isabella", "Fernando", "Camila", "Rafael",
        "Wendy",
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

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

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


    def mostrar_dinheiro(self):
        print(f'Você possui ${self.dinheiro}')


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'{self} ganhou ${quantidade}')
        self.mostrar_dinheiro()


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
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
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


    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'Um {pokemon} selvagem apareceu!')

            escolha = input('Deseja capturar esse pokemon? (s/n): ')
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f'{pokemon} fugiu!')
            else:
                print('OK, boa viagem! ')

        else:
            print('Essa exploração não deu em nada! ')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=None, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=None, pokemons=pokemons)





