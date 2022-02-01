s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o {} valor: '.format(c)))
    if n%2 == 0:
        s += n
        cont += 1
print('Voce informou {} valores pares e a soma é {}'.format(cont, s))
