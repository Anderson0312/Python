cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um numerp [999 para para]: '))
    if n != 999:
        cont += 1
        soma += n
print('Voce digitou {} números e a soma entre eles foi {}'.format(cont, soma))