listatodos = list()
listapar = list()
listaimpar = list()
while True:
    n = int(input(('Digite um numero: ')))
    soun = str(input('Quer contiunuar? [S/N] ')).upper().strip()[0]
    print('-=' * 30)
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 == 1:
        listaimpar.append(n)
    listatodos.append(n)
    if soun in 'N':
        break
print(f'A lista completa é {listatodos}')
print('-=' * 30)
print(f'A lista de pares é {listapar}')
print('-=' * 30)
print(f'A lista de impares é {listaimpar}')