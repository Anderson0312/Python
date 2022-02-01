print('-=' * 15)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-=' * 15)
total = cont1000 = menor = cont = 0
nomemenor = ''
while True:
    nomeP = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    soun = ' '
    print('-' * 30)
    while soun not in 'SN':
        soun = str(input('Quer Continuar? [S/N]')).strip()[0].upper()
        print('-' * 30)
    total += preco
    if preco >= 1000:
        cont1000 += 1
    if cont == 1:
        menor = preco
        nomemenor = nomeP
    else:
        if preco < menor:
            menor = preco
            nomemenor = nomeP
    if soun == 'N':
        break
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {cont1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomemenor} que custa {menor:.2f}')