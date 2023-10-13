import random

from time import sleep

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

    def __init__(self, nome=None, pokemons=[], dinheiro=100, pokebolas=5, dia=1):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

        self.pokebolas = pokebolas

        self.dia = dia

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(' ')
            print(f'Pokémons de >> {self} << ')
            print(f'Você tem {len(self.pokemons)} Pokémons')
            print('~' * 30)
            for i, pokemon in enumerate(self.pokemons):
                print(f'{i} - {pokemon}')
        else:
            print(f'{self} não tem pokémons')


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido} para a batalha! ')
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não possui Pokemons!')


    # def excluir_pokemon(self, pokemon_excluir):
    #     try:
    #         self.pokemons.remove(pokemons)
    #         print(' ')
    #         print(f'>>>>>> Pokémon {pokemon_excluir} excluido com sucesso!')
    #         print(' ')
    #     except KeyError:
    #         print('>>>>>> Pokémon inexistente!')
    #     except Exception as error:
    #         print(f'Um erro inesperado ocorreu! ERRO: {error}')


    def mostrar_dinheiro(self):
        print(f'DINHEIRO: ${self.dinheiro:.2f}')


    def mostrar_pokebolas(self):
        print(f'POKEBOLAS: {self.pokebolas}')


    def mostrar_dia(self):
        print(f'DIA: {self.dia}')


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'{self} ganhou ${quantidade:.2f}')
        self.mostrar_dinheiro()


    # def perder_dinheiro(self, quantidade):
    #     self.dinheiro -= quantidade
    #     print(f'{self} perdeu ${quantidade}')
    #     self.mostrar_dinheiro()


    def ganhar_pokebolas(self, quantidade):
        self.pokebolas += quantidade
        print(f'{self} ganhou {quantidade} pokebolas')
        self.mostrar_pokebolas()


    def add_dias(self,quantidade):
        self.dia += quantidade


    def batalhar(self, pessoa):
        print('==' * 30)
        print(f'>>>>>>>> {self} iniciou uma batalha com {pessoa} <<<<<<<<')
        print('==' * 30)

        pessoa.mostrar_pokemons()
        print('-' * 30)
        pokemon_inimigo = pessoa.escolher_pokemon()
        print('-' * 30)

        pokemon_player = self.escolher_pokemon()
        print('-' * 30)

        if pokemon_player and pokemon_inimigo:
            while True:
                vitoria = pokemon_player.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} GANHOU A BATALHA!')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 1.5) # <- quantidadde de dinheiro ganho
                    self.ganhar_pokebolas(random.randint(0, 5))
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon_player)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha!')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 0.8) # <- quantidadde de dinheiro ganho
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
        if self.pokebolas > 0:
            print('Explorando...')
            sleep(3)
            if random.random() <= 0.8: #chance de aparecer pokemon
                pokemon = random.choice(POKEMONS)
                print(f'Um {pokemon} selvagem apareceu!')
                try:
                    escolha = input('Deseja capturar esse pokemon? (s/n): ')
                    if escolha == 's':
                        print('Capturado...')
                        sleep(3)
                        if random.random() >= 0.1: #chance de captura
                            self.capturar(pokemon)
                            self.pokebolas -= 1
                        else:
                            print(f'{pokemon} fugiu!')
                            self.pokebolas -= 1
                    else:
                        print('OK, boa viagem! ')
                except:
                    print('>>>>> Opção invalida')
            else:
                print('Essa exploração não deu em nada! ')
                sleep(1.5)
        else:
            print('>>>>> Você não tem pokebolas para explorar')




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





