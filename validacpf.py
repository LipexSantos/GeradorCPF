import re
from random import randint


def removedor_caractere(cpf):
    return re.sub(r'[^0-9]', '', cpf)  # r é para tratar a / ou caracteres especias


def validar_cpf(cpf):
    cpf = removedor_caractere(cpf)
    # Elimina os dois últimos digitos do CPF
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        # Decrementa o contador reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            # Formula
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    # Evita sequências. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também adicionei essa checagem aqui.
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False


def gerador_cpf():
    cpf = str(randint(100000000, 999999999))
    novo_cpf = cpf
    cont = 10
    total = 0
    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * cont

        cont -= 1
        if cont < 2:
            cont = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if validar_cpf(novo_cpf):
        print(f'CPF: {novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]} = Válido')
    else:
        print(f'CPF: {novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]} = Inválido')


if __name__ == '__main__':
    opcao = int(input('[1] - Gerar CPF\n'
                      '[2] - Validar CPF\n'
                      'Escolha sua Opcao: '))
    print('%' * 30)
    if opcao == 1:
        gerador_cpf()
    if opcao == 2:
        cpf = input('Digite CPF: ')
        if validar_cpf(cpf):
            print('CPF Válido')
        else:
            print('Cpf Inválido')


