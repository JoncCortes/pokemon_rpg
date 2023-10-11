from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, Escolha o Pokemon que irá te acompanhar em sua jornada!')

    pikachu = pokemonEletrico('Pikachu', level=1)
    charmander = pokemonFogo('Charmander', level=1)
    squirtle = pokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('[ 1 ]', pikachu)
    print('[ 1 ]', charmander)
    print('[ 1 ]', squirtle)

    while True:
        escolha = input('Escolha seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')


player = Player('Jon')
player.capturar(pokemonFogo('Charmander', level=1))

inimigo1 = Inimigo(pokemons=[pokemonAgua('Squirtle', level=1)])

player.batalhar(inimigo1)