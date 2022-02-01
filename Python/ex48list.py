numeros = [2, 5, 6, 7]
numeros[2] = 3
numeros.append(8)  # para adicionar um elemento a lista
numeros.sort()  # para organizar a lista em ordem alfabetica ou crescente
numeros.insert(2, 0)  # para inserir um item na lista na posiçõa desejada [posição, elemento]
numeros.pop(2)  # para apagar um indice da lista
if 4 in numeros:
    numeros.remove(2)  # remove o elemento da lista desejado
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos')

valores = list()
valores.append(5)
valores.append(3)
valores.append(6)

for v in valores:
    print(f'{v}...', end='')

for pos, valo in enumerate(valores):
    print(f'\nNa posição {pos} encontrei o valor {valo}!')
print('Cheguei ao final da lista.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
