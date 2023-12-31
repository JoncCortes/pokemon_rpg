import pickle

from time import sleep
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(' ')
    print(f'Olá {player}, Escolha o Pokemon que irá te acompanhar em sua jornada!')

    pikachu = pokemonEletrico('Pikachu', level=1)
    charmander = pokemonFogo('Charmander', level=1)
    squirtle = pokemonAgua('Squirtle', level=1)
    print(' ')
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
            print('>>>>> Escolha inválida')


def save_game(player):
    try:
        with open('database.db', 'wb') as file:
            pickle.dump(player, file)
            print('>>>>> Jogo salvo com sucesso!')
    except Exception as error:
        print('>>>>> Erro ao salvar jogo')


def load_game():
    try:
        with open('database.db', 'rb') as file:
            player = pickle.load(file)
            print('>>>>> Jogo carregado com sucesso!')
            return player
    except Exception as error:
        print('>>>>> Save não encontrado')


def shop():
    while True:
        sleep(1.5)
        print('=#' * 30)
        print('Bem-vindo a Loja pokémon')
        print('--' * 30)
        print('O que deseja comprar?')
        print('[ 1 ] POKEBOLA : $200')
        print('[ 2 ] -------- : FORA DE ESTOQUE')
        print('[ 3 ] -------- : FORA DE ESTOQUE')
        print('[ 0 ] Sair da loja')
        opcao = input('Sua escolha: ')

        if opcao == '1':
            quantidade = int(input('Quantas pokebolas deseja comprar: '))
            if player.dinheiro >= 200 * quantidade:
                player.pokebolas += quantidade
                player.dinheiro -= 200 * quantidade
                print('-' * 15)
                print(f'{quantidade} Pokebolas compradas com sucesso!')
                print('-' * 15)
                break
            else:
                print('-' * 15)
                print('Você não tem dinheiro suficiente!')
                print('-' * 15)
        elif opcao == '2':
            print('-' * 15)
            print('Produto fora de estoque')
            print('-' * 15)
        elif opcao == '3':
            print('-' * 15)
            print('Produto fora de estoque')
            print('-' * 15)
        elif opcao == '0':
            break
        else:
            print('-' * 15)
            print('Opção invalida')
            print('-' * 15)




if __name__ == '__main__':
    print('=#' * 50)
    print('''
⠐⣶⣾⣭⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡄⠀⠄⠀⠀⠀⠀⠀
⠀⠹⣿⣿⣧⠈⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⢻⣿⣿⣿⢇⠀⠀⠀⠀⠀
⠀⠀⠘⢿⣿⡄⠀⠀⠀⠙⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠉⠀⠀⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣧⠀⠀⠀⠀⠀⠙⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠀⠀⢰⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢷⣀⠀⠀⠀⠀⠀⠹⣦⡀⠀⢀⣀⣀⣀⣰⣶⣦⣀⣀⡀⠀⠀⣠⡶⠋⠁⠀⠀⠀⠀⠀⢀⣾⡻⠋⠀⠀⡀⣀⣄⣤⡤⣦
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠈⣷⠶⠛⠉⠉⠁⠀⠀⠈⠉⠉⠛⠿⡿⠟⠁⠀⠀⠀⠀⢀⣠⣶⡿⠋⣀⣤⠼⠗⠛⠉⠁⠀⠀⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠷⢦⣀⣰⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣤⣶⣟⣣⡽⡿⠟⠋⠀⠀⠀⠀⠀⠀⢀⣾⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⡷⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⣯⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣴⣿⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⣴⡻⣿⣷⡀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⣿⡿⢿⣿⠃⠀⠀⠀⣀⣀⠀⠀⠀⣿⣿⣿⣿⠇⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣾⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡤⣤⡈⠉⠉⠁⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠉⠛⠃⢀⣠⣈⣧⠀⠀⣤⣴⡶⠿⠿⠛⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠙⣦⠀⠀⠀⠳⠤⠴⠞⠛⠦⣤⠾⠃⠀⠀⣼⠋⠀⠈⣿⠀⠀⠈⣷⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠄⠀⣰⡟⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣶⣛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢒⣶⣿⢻⣷⣤⠀⠀⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠙⠳⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠋⢸⡷⠞⠋⠀⣀⣠⣶⠞⠿⠙⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠉⠓⠭⣷⣦⣤⣤⡴⠦⣺⠛⠉⠀⠀⠀⠈⣷⠀⢶⣿⣟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠘⣷⣀⣨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣄⣀⣠⡟⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⢀⡇⠀⠘⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣛⣿⣁⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⢸⣱⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⠻⣤⣉⠷⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⣿⠰⠠⡏⠀⠀⠀⠀⠀⠀⣰⠇⠀⢀⡴⢛⣱⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⢷⡀⠈⠳⣄⠀⠹⣦⠀⠀⠀⠀⠀⠀⡟⠀⠀⣷⠀⠀⠀⠀⠀⣰⠏⠀⢀⣴⠚⠉⣸⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⡀⠈⠃⣦⠘⢷⡀⠀⠀⠀⢀⣧⣤⣤⣿⠀⠀⠀⢀⣼⠃⣀⠒⠛⢀⣤⣾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣛⣦⠴⢿⢶⣿⣿⡤⢴⣶⢿⡛⠁⠙⣿⣶⣤⣤⣾⣗⢶⣯⣤⣴⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    print('=#' * 50)
    print('                         Bem-vindo ao POKÉMON RPG baseado em texto')
    print('                              Criado por Jonas Cortes © 2023')
    print('=#' * 50)
    sleep(2)

    player = load_game()

    if not player:
        nome = input(('Olá, qual seu nome? '))
        player = Player(nome)
        sleep(1.5)
        print(f'{player}, esse é um mundo habitado por fantasticas criaturas chamadas POKÉMONS')
        sleep(2.5)
        print('Sua missão é batalhar contra seus inimigos e CAPTURAR todos eles!')
        sleep(2.5)
        print('Se conseguir capturar todos os Pokémons, você se tornará um MESTRE POKÉMON!')
        sleep(2.5)

        if player.pokemons:
            print('-' * 30)
            print('Já ví que você tem alguns pokémons')
            sleep(1.5)
            player.mostrar_pokemons()
        else:
            print('-' * 30)
            print('Você ainda não tem nenhum pokémon, escolha um:')
            print('-' * 30)
            sleep(1.5)
            escolher_pokemon_inicial(player)
            sleep(2)

        print('-' * 30)
        print('Pronto, agora que já tem seu Pokémon, prepare-se para sua primeira batalha pokémon!')
        sleep(3)

        primeiro = Inimigo(pokemons=[pokemonAgua('Squirtle', level=1)])
        player.batalhar(primeiro)
        print('Agora que já sabe como batalhar, está livre para explorar ou continuar batalhando!')
        save_game(player)

    while True:
        sleep(1.5)
        print(' ')
        print('=#' * 30)
        player.mostrar_dia()
        print('-' * 30)
        print('O que deseja fazer agora?')
        print('[ 1 ] Explorar o mundo')
        print('[ 2 ] Batalha de treinadores')
        print('[ 3 ] Pokémons')
        print('[ 4 ] Bolsa')
        print('[ 5 ] Loja')
        print('[ 0 ] Sair do jogo')
        print('=#' * 30)
        escolha = input('>>>>> sua opção: ')

        if escolha == '0':
            print('>>>>> Saindo do Jogo...')
            sleep(2)
            break
        elif escolha == '1':
            player.explorar()
            player.add_dias(1)
            save_game(player)
        elif escolha == '2':
            inimgo_aleatorio = Inimigo()
            player.batalhar(inimgo_aleatorio)
            player.add_dias(1)
            save_game(player)
        elif escolha == '3':
            player.mostrar_pokemons()
            print('-' * 30)
            print('[ 1 ] Excluir Pokémon')
            print('[ 0 ] Voltar')
            opcao = input('Sua Opção: ')
            if opcao == '1':
                pokemon_del = int(input('Digite o número do Pokémon: '))
                player.excluir_pokemon(pokemon_del)
                save_game(player)
                player.mostrar_pokemons()
            else:
                continue


        elif escolha == '4':
            print('===== SUA BOLSA =====')
            player.mostrar_dinheiro()
            player.mostrar_pokebolas()

        elif escolha == '5':
            shop()
        else:
            print('>>>>> Opção invalida')
