numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    for n in numeros:
        if numeros.count(n) >= 2:
            numeros.remove(n)
            print('O numero ja existe na lista então não sera colocado')
        else:
            print('Valor adicionado com sucesso..')
    print('-=' * 20)
    soun = str(input('Quer continuar? [S/N] ')).strip()[0]
    print('-=' * 20)
    if soun in 'Nn':
        break
print(f'Os valores digitados foram: {sorted(numeros)}')