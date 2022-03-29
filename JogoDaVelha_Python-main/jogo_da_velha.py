from time import sleep


def mostrar_jogo():  # Mostra a matriz
    letras = ['A', 'B', 'C']
    print('   1   2   3')
    for ind, linha in enumerate(lista):
        print(letras[ind], end='')
        print('|', end=' ')
        for c in range(3):
            if linha[c] == 'X':
                print('X', end=' ')
            elif linha[c] == 'O':
                print('O', end=' ')
            else:
                print(linha[c], end=' ')
            print('|', end=' ')
        print()
    sleep(0.5)


def entradados():  # Verifica se os valores de entrada são válidos, e os insere na matriz
    coluna = linha = 8
    linhateste = colunateste = False
    linha1 = ''
    while True:
        while not linhateste:  # verifica se os dados inseridos para linha são válidos
            while True:
                linha1 = input('Linha (A, B, C ou "FIM"): ').lower()
                if linha1 == '':
                    print('Nenhum valor digitado!')
                    mostrar_jogo()
                    continue
                else:
                    break
            if linha1 in 'abcfim':
                if linha1 == 'a':
                    linha = 0
                    linhateste = True
                elif linha1 == 'b':
                    linha = 1
                    linhateste = True
                elif linha1 == 'c':
                    linha = 2
                    linhateste = True
                else:
                    verificar(True)
                    break
            else:
                print('Digite apenas A, B, C ou FIM ')
                mostrar_jogo()
                continue
        if linha1 == 'fim':  # finaliza a função entradadados e encerra o programa
            break
        while not colunateste:  # verifica se os dados inseridos para coluna são válidos
            try:
                coluna = int(input('Coluna (1, 2 ou 3): ')) - 1
            except ValueError:
                print('Nenhum valor digitado.')
                mostrar_jogo()
                continue
            if 0 <= coluna <= 2:
                colunateste = True
            else:
                print('Digite um número entre 1 e 3 (inclusive)')
                mostrar_jogo()
                continue

        if lista[linha][coluna] == 'X' or lista[linha][coluna] == 'O':  # verifica se a posição não está ocupada
            print("Essa posição já está ocupada.")
            colunateste = linhateste = False
            mostrar_jogo()
        else:
            if player_x_turn:
                lista[linha][coluna] = 'X'
            else:
                lista[linha][coluna] = 'O'
            sleep(0.5)
            print()
            break


def verificar(finish=False):  # Verifica se houver ganhador após uma jogada
    def ganhador():  # Mostra uma mensagem determinando o vencedor
        if not player_x_turn:
            print('-' * 22)
            print("VENCEDOR: 'X' {:>8}".format(nome_x))
            print('-' * 22)
        elif player_x_turn:
            print('-' * 22)
            print("VENCEDOR: 'O' {:>8}".format(nome_o))
            print('-' * 22)

    global fim

    if finish:
        fim = True
        return
    # o if abaixo verifica se houve jogada vencedora na diagonal
    if (lista[0][0] == lista[1][1] == lista[2][2] or lista[0][2] == lista[1][1] == lista[2][0]) and (
            lista[0][0] != '_' and lista[1][1] != '_' and lista[2][2] != '_' or
            lista[0][2] != '_' and lista[1][1] != '_' and lista[2][0] != '_'):
        fim = True
        ganhador()
    # o for abaixo verifica se houve alguma jogada vencedora na horizontal
    for linha in lista:
        if not '_' in linha:
            if len(set(linha)) == 1:
                ganhador()
                fim = True
                break
    # o for abaixo verifica se houve alguma jogada vencedora na vertical
    for c in range(3):
        if lista[0][c] == lista[1][c] == lista[2][c] and lista[0][c] != '_':
            ganhador()
            fim = True
            break

    total = 0
    for linha in lista:
        for c in range(3):
            if linha[c] in 'XO':
                total += 1

    if total == 9:
        print('-' * 27)
        print(f"{'NÃO HOUVE VITORIOSO':^27}")
        print('-' * 27)
        fim = True


def player_x():  # aciona a função ""entrardados" para o jogador X
    print(f"Vez do jogador {nome_x} 'X': ")
    entradados()
    return False


def player_o():  # aciona a função ""entrardados" para o jogador O
    print(f"Vez do jogador {nome_o} 'O': ")
    entradados()
    return True


def titulo():
    print(' ' * 15, "=" * 30)
    print(' ' * 15, f'{" JOGO DA VELHA ":-^30}')
    print(' ' * 15, "=" * 30)
    print()
    print('COMO JOGAR: Após inserir os nomes de dois jogadores, deve-se\n'
          'inserir a linha e coluna desejada a cada jogada. Para encerrar\n'
          'o jogo antes do fim, basta digitar "fim" em vez de informar a linha.')


titulo()
mostra_titulo = False
continuar = True
while continuar:
    if mostra_titulo:
        titulo()
    print()
    nome_x = input('Nome do jogador X: ').title()
    nome_o = input('Nome do jogador O: ').title()
    lista = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print()
    mostrar_jogo()  # Mostra a matriz no inicial
    print()
    player_x_turn = True  # Controla a vez de cada jogador
    fim = False  # Enquanto False, o jogo não acaba

    while True:
        if player_x_turn:
            player_x_turn = player_x()  # Após o jogador 'X' jogar, esta variável recebe False
        else:
            player_x_turn = player_o()  # Após o jogador 'O' jogar, esta variável recebe True

        mostrar_jogo()  # Mostra a matriz do jogo a cada jogada
        print()
        verificar()  # Função verifica a cada jogada se algum jogador ganhou
        if fim:
            continuar = input('Jogar novamente? [s/n] ')
            print()
            if continuar in 'Nn':
                continuar = False
                break
            else:
                mostra_titulo = True
                break
