numeros = list()
for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))
print(f'Voce digitou os valores {numeros}')
print('O maior valor digitado foi {} nas possições'.format(max(numeros)), end=' ')

'''
No for
O pos foi usado para fixar a localização
o v foi usado para fixar os valores
e o enumerate para enumerar a lista informada

No if 
usamos se o v = valor for igual ao maior da lista, mostrar a posição na lista +1
'''

for pos, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{pos+1}', end=' ')
print('\nO menor numero digitado foi {} nas posições'.format(min(numeros)), end=' ')
for pos, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{pos + 1}', end=' ')

