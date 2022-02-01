n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair do programa')
    opc = int(input('>>>> Qual é sua opção? '))
    if opc == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opc == 2:
        mult = n1 * n2
        print('O resultado de {} * {} é {}'.format(n1, n2, mult))
    elif opc == 3:
        if n1 > n2:
            print('O numero {} é o maior.'.format(n1))
        elif n2 > n1:
            print('O numero {} é maior'.format(n2))
    elif opc == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif opc == 5:
        print('Fim do programa!')
    else:
        print('Tente novamente informe uma das opções validas!')
