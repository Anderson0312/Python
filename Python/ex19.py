n = int(input('Digite um número: '))
mult = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, mult))
if mult == 2:
    print('\né primo')
else:
    print('Não é primo')
