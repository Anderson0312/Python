from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
soma = cont = 0
while True:
    seuvalor = int(input('Digite um valor: '))
    poui = str(input('Par ou Impar? [P/I] ')).strip()[0]
    aleatorio = randint(1, 9)
    soma = seuvalor + aleatorio
    print('-' * 50)
    print(f'Voce jogou {seuvalor} e o computador {aleatorio}. o total de {soma} e deu ', end='')
    if soma % 2 == 0:
        print('PAR')
        print('-' * 50)
        if poui in 'Pp':
            print('Você VENCEU')
            print('-' * 50)
        else:
            print('Você PERDEU')
            break
    else:
        print('IMPAR')
        print('-' * 50)
        if poui in 'Ii':
            print('Você VENCEU')
            print('-' * 50)
        else:
            print('Você PERDEU')
            break
    cont += 1
    print('Vamos jogar novamente! ')
    print('-' * 50)
print(f'GAMER OVER! você ganhou {cont} vezes do computador. ')

