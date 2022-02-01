produtos = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.98,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-'*43)
print('{:^43}'.format('LISTAGEM DE PREÇOS'))
print('-'*43)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]:>10.2f}')
print('-'*43)


