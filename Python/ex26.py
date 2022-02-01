from random import randint
print('''Sou se computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue aivinhar qual foi?''')
pcp = randint(0, 10)
palpite = 0
cont = 0
while palpite is not pcp:
    palpite = int(input('Qual é seu palpite?'))
    cont += 1
    if pcp > palpite:
        print('Mais.. tente novamente.')
    elif pcp < palpite:
        print('Menos.. tente novamente.')
print('Você acertou com {} tentativas o numero escolhido foi {}.'.format(cont, pcp))

