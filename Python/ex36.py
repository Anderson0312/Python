mult = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 35)
    if valor < 0:
        break
    for c in range(1, 11):
        mult = c * valor
        print(f'{valor} x {c} = {mult}')
    print('-' * 35)
print('PROGRAMAR TABUADA ENCERRADO. Volte sempre! ')