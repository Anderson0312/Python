print('-' * 30)
print('      CADASTRE UMA PESSOA')
print('-' * 30)
contid = conth = contfmenor = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 30)
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        contid += 1
    if sexo in 'Mm':
        conth += 1
    if sexo in 'Ff':
        if idade <= 20:
            contfmenor += 1
    if soun in 'Nn':
        break
print(f'O total de pessoas com mais de 18 anos é: {contid}.')
print(f'Ao todo temos {conth} homens cadastrados.')
print(f'E temos {contfmenor} mulhers com menos de 20 anos.')