from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, Escolha o Pokemon que irá te acompanhar em sua jornada!')

    pikachu = pokemonEletrico('Pikachu', level=1)
    charmander = pokemonFogo('Charmander', level=1)
    squirtle = pokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('[ 1 ]', pikachu)
    print('[ 2 ]', charmander)
    print('[ 3 ]', squirtle)

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


if __name__ == '__main__':
    print('=#' * 30)
    print('Bem-vindo ao POKEMON RPG baseado em texto ')
    print('Criado por Jonas Cortes © 2023')
    print('=#' * 30)

    nome = input(('Olá, qual seu nome? '))
    player = Player(nome)
    print(f'{player}, esse é um mundo habitado por fantasticas criaturas chamadas POKÉMONS')
    print('Sua missão é batalhar contra seus inimigos e CAPTURAR todos eles!')
    print('Se conseguir capturar todos os Pokémons, você se tornará um MESTRE POKÉMON!')
    player.mostrar_dinheiro()

    if player.pokemons:
        print('Já ví que você tem alguns pokémons')
        player.mostrar_pokemons()
    else:
        print('Você ainda não tem nenhum pokémon, escolha um:')
        escolher_pokemon_inicial(player)

    print('Pronto, agora que já tem seu Pokémon, enfrente seu rival em uma batalha!')

    gary = Inimigo('Gary', pokemons=[pokemonAgua('squirtle', level=1)])
    player.batalhar(gary)

    while True:
        print('=#' * 30)
        print('O que deseja fazer agora?')
        print('[ 1 ] Explorar o mundo')
        print('[ 2 ] Batalha de treinadores')
        print('[ 0 ] Sair do jogo')
        escolha = input('sua opção: ')

        if escolha == '0':
            break
        elif escolha == '1':
            player.explorar()
        elif escolha == '2':
            inimgo_aleatorio = Inimigo()
            player.batalhar(inimgo_aleatorio)
        else:
            print('Opção invalida')
