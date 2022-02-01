p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
decimo = p1 +(10 - 1) * rz
for c in range(p1, decimo+1, rz):
    print('{}'.format(c), end=' ⇀ ')
print('ACABOU!!!')