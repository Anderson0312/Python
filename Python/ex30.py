print('Gerador de PA')
print('==============')
p1 = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
primeiro = p1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print('{} > '.format(primeiro), end='')
        c += 1
        primeiro += rz
    print('PAUSA')
    mais = int(input('Mais quantos termos voce deseja? '))
print('Progressão finalizada com {} termos.'.format(total))
