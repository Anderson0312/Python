'''from math import factorial
n1 = int(input('Digite um numero para
calcular seu fatorial:'))
f = factorial(n1)
print('Calculando {}! = {} '.format(n1, f))'''

n = int(input('Digite um numero para calcular seu factorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')