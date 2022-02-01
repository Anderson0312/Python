from random import choice
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
opc = int(input('Qual é sua jogada? '))
lista = [0, 1, 2]
aleatorio = choice(lista)
if aleatorio == opc:
    print('Deu empate jogue novamente!')
elif aleatorio == 0 and opc == 1:
    print('O cumputador escolheu PEDRA')
    print('Você escolheu PAPEL')
    print('VOCE VENCEU')
elif aleatorio == 0 and opc == 2:
    print('O cumputador escolheu PEDRA')
    print('Você escolheu TESOURA')
    print('VOCE PERDEU')
elif aleatorio == 1 and opc == 0:
    print('O cumputador escolheu PAPEL')
    print('Você escolheu PEDRA')
    print('VOCE PERDEU')
elif aleatorio == 1 and opc == 2:
    print('O cumputador escolheu PAPEL')
    print('Você escolheu TESOURA')
    print('VOCE VENCEU')
elif aleatorio == 2 and opc == 0:
    print('O cumputador escolheu TESOURA')
    print('Você escolheu PEDRA')
    print('VOCE VENCEU')
elif aleatorio == 2 and opc == 1:
    print('O cumputador escolheu TESOURA')
    print('Você escolheu PAPEL')
    print('VOCE PERDEU')


