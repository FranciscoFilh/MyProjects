from random import randint
from time import sleep


def Opcoes():
    print("Escolha uma das opções:")
    print("[{}1{}] - Pedra".format(cores['branco'], cores['limpa']))
    print("[{}2{}] - Papel".format(cores['branco'], cores['limpa']))
    print("[{}3{}] - Tesoura".format(cores['branco'], cores['limpa']))
    print("[{}0{}] - Finalizar partida\n".format(cores['branco'], cores['limpa']))


def Validacao():  # Vai validar se a jogada é um numero

    while True:
        x = input("Sua jogada: ")

        if x.isnumeric() is True:
            x = int(x)
            return x

        else:
            print('')
            print((f"{cores['azul']}-{cores['limpa']}" * 65))
            print("Jogada inválida! [1 - Pedra / 2 - Papel / 3 - Tesoura / 0 - Sair]")
            print((f"{cores['azul']}-{cores['limpa']}" * 65))


def JogadaUser(cont_partida, cont_rodada, lim):
    print('')
    sleep(0.5)
    print("{}*****{}".format(cores['azul'], cores['limpa']), end='')
    print(f'\033[30m Partida {cont_partida} - {cont_rodada + 1}/{lim} \033[m', end='')
    print("{}*****{}".format(cores['azul'], cores['limpa']))

    while True:
        jogUser = Validacao()
        print('')

        # Convertendo o comando do usuário
        # Pedra = 0 / Papel = 1 / Tesoura = 2 / Sair = 3

        if 0 < jogUser < 4:
            jogUser -= 1
            break

        elif jogUser == 0:
            return 3

        else:
            print((f"{cores['azul']}-{cores['limpa']}" * 65))
            print("Jogada inválida! [1 - Pedra / 2 - Papel / 3 - Tesoura / 0 - Sair]")
            print((f"{cores['azul']}-{cores['limpa']}" * 65))

    resultado = Rodada(jogUser)
    sleep(0.5)

    if resultado == 0:
        print("Voce Ganhou".center(27))
        return 0

    elif resultado == 1:
        print("Voce Perdeu".center(27))
        return 1

    else:
        print("Empate".center(27))
        return 2


def Rodada(jogada_usuario):
    jogadaPc = randint(0, 2)
    listaJogadas = ['PEDRA', 'PAPEL', 'TESOURA']

    string1 = (listaJogadas[jogada_usuario] + '  X  ' + listaJogadas[jogadaPc]).center(27)

    print(f"{cores['preto']}{string1}{cores['limpa']}")

    #  Pedra
    if jogada_usuario == 0:
        if jogadaPc == 0:
            return 2
        elif jogadaPc == 1:
            return 1
        else:
            return 0

    #  Papel
    elif jogada_usuario == 1:
        if jogadaPc == 0:
            return 0
        elif jogadaPc == 1:
            return 2
        else:
            return 1

    #  Tesoura
    else:
        if jogadaPc == 0:
            return 1
        elif jogadaPc == 1:
            return 0
        else:
            return 2


def Partida(contador_part):  # Uma partida equivale a 3 rodadas
    contadorRod = 0
    limite = 3  # Numero de rodadas da partida
    listaRodadas = []

    while contadorRod < limite:
        resulRodada = JogadaUser(contador_part, contadorRod, limite)

        if resulRodada == 2:
            continue
        elif resulRodada == 3:
            return 3
        else:
            listaRodadas.append(resulRodada)
            contadorRod += 1

        if listaRodadas.count(0) == 2 or listaRodadas.count(1) == 2:
            break

    sleep(0.5)
    print('')

    # Resultado da partida
    if listaRodadas.count(0) > listaRodadas.count(1):
        print(f"{cores['azul']}*" * 27)
        print(f"*{cores['limpa']}" + " " * 8 + f"{cores['branco']}PARABÉNS!{cores['limpa']}"
              + " " * 8 + f"{cores['azul']}*")
        print(f"{cores['azul']}*{cores['limpa']}" * 27)
        return 0
    else:
        print(f"{cores['azul']}*" * 27)
        print(f"*{cores['limpa']}" + " " * 8 + f"{cores['branco']}GAME OVER{cores['limpa']}"
              + " " * 8 + f"{cores['azul']}*")
        print(f"{cores['azul']}*{cores['limpa']}" * 27)
        return 1


def Repet():

    while True:

        resposta = input("\nIniciar nova partida? [s/n]: ")
        resposta = resposta.lower()
        print((f"{cores['azul']}-{cores['limpa']}" * 27))

        if resposta == 's':
            return 0
        elif resposta == 'n':
            return 1
        else:
            print("\nInvalido!")


contador_partidas = 1
listaPartidas = []
pontinhos = ['.', '.', '.']
cores = {'limpa': '\033[m',
         'azul': '\033[36m',
         'branco': '\033[1;30m',
         'preto': '\033[7;30m'}

print(('{}~{}'.format(cores['azul'], cores['limpa'])) * 27)
print("{}JO KEN PÔ{}".center(27).format(cores['branco'], cores['limpa']))
print(('{}~{}'.format(cores['azul'], cores['limpa'])) * 27)
print('\n')
sleep(0.5)

Opcoes()

while True:
    resul_patida = Partida(contador_partidas)

    # Saida no meio da partida
    if resul_patida == 3:
        print('')
        print(f"{cores['preto']}Encerrando".center(25), end='')
        for pnt in pontinhos:
            sleep(1)
            print(f"{cores['preto']}{pnt}{cores['limpa']}", end='')
        print('')
        break
    else:
        listaPartidas.append(resul_patida)

    repet = Repet()

    if repet == 0:
        contador_partidas += 1
    # Saida na próxima rodada
    else:
        print('')
        print(f"Você jogou {contador_partidas} partidas e ganhou em {listaPartidas.count(0)} delas.\n")
        sleep(0.2)
        print(f"{cores['preto']}Encerrando".center(25), end='')

        for pnt in pontinhos:
            sleep(1)
            print(f"{cores['preto']}{pnt}{cores['limpa']}", end='')

        print('')
        break
