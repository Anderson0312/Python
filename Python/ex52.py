lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    soun = str(input('Quer continuar? [S/N] '))
    print('-=' * 30)
    if soun in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print('-=' * 30)
print('Os valores em ordem decrescente são {}'.format(lista))
print('-=' * 30)
if 0 >= lista.count(5):
    print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')