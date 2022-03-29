def valida_cpf(cpf):
    while True:
        for num in cpf:
            if not num.isnumeric():
                print('Digite APENAS números.')
                print()
                return False
        if len(cpf) != 11:
            print('Erro: Não foram digitados 11 dígitos.')
            print()
            return False
        soma1 = soma2 = 0
        multi1 = 10
        multi2 = 11
        for c in range(0, 9):
            soma1 += int(cpf[c]) * multi1
            multi1 -= 1
        for c in range(0, 10):
            soma2 += int(cpf[c]) * multi2
            multi2 -= 1

        if 11 - (soma1 % 11) != int(cpf[9]) or 11 - (soma2 % 11) != int(cpf[10]):
            print('CPF INVÁLIDO! Digite novamente')
            print()
            return False
        else:
            print()
            print(f'CPF VÁLIDO: ', end='')
            for c in range(3):
                print(cpf[c], end='')
            print('.', end='')
            for c in range(3, 6):
                print(cpf[c], end='')
            print('.', end='')
            for c in range(6, 9):
                print(cpf[c], end='')
            print('-', end='')
            for c in range(9, 11):
                print(cpf[c], end='')
            print()
            return True


def mostrar_titulo():
    print('=' * 24)
    print(f'{"VALIDADOR DE CPF": ^24}')
    print('=' * 24)


titulo = True
while True:
    if titulo:
        mostrar_titulo()
    titulo = False
    numero_cpf = input('CPF (apenas números): ')
    if valida_cpf(numero_cpf):
        continuar = input('Executar novamente? [s/n] ').lower()
        titulo = True
        print()
        if continuar == 'n':
            break
