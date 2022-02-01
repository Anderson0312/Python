print('Gerador de PA')
print('=================')
p1 = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
primeiro = p1
c = 1
while c < 10:
    print('{} > '.format(primeiro), end='')
    c += 1
    primeiro += rz
print('FIM.', end='')
