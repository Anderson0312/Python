print('--'*15)
print('Sequencia de Fibonacci')
print('--'*15)
n = int(input('Quantos termos você quer mostrar? '))
print('~~'*15)
t1 = 0
t2 = 1
cont = 3
print('{} > {}'. format(t1, t2), end='')
while n >= cont:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(' > {}'.format(t3), end='')
print(' > FIM!')


