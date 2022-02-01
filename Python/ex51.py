numeros = list()

for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or n > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na pos {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')