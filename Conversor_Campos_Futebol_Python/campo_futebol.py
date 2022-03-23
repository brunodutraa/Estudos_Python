from time import sleep
def mostrar_campo(tamanho=0.0):
    if tamanho != 0:
        sleep(0.6)
        print()
        print('', '_' * 19, '\n|___      |      ___|\n|_  |     |     |  _|')
        print(f'|_|º|)  ( º )  (|º|_|   X {tamanho:.1f}')
        print('|___|     |     |___|\n|_________|_________|')
        sleep(1)
        print(f'EQUIVALENTE A {tamanho:.1f} CAMPOS DE FUTEBOL')
    else:
        print('', '_' * 19, '\n|___      |      ___|\n|_  |     |     |  _|')
        print('|_|o|)  ( o )  (|o|_|\n|___|     |     |___|\n|_________|_________|')
        print()


mostrar_campo()
while True:
    opcao = int(input('Digite a conversão desejada:\n1 - Hectares\n2 - Metros quadrados\n3 - Sair\n'))
    if opcao == 1:
        hectares = float(input('Quantidade de hectares: '))
        mostrar_campo(hectares * 0.71)
    elif opcao == 2:
        metros = float(input('Tamanho em metros quadrados: '))
        mostrar_campo((metros / 10000) * 0.71)
    elif opcao == 3:
        print('Encerrando...')
        sleep(0.7)
        break
    else:
        print('Opção inválida.')
        continue
    print()

    continuar = input('Continuar? [s/n]').lower()
    if continuar == 's':
        print()
        mostrar_campo()
    elif not continuar in 'sn':
        print()
        print('Opção inválida')
    else:
        print('Encerrando...')
        sleep(0.7)
        break



