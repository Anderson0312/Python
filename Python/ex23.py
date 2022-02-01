listidade = []
maiorh = 0
mulher20 = 0
nomevelho = ''
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M':
        if idade == 1:
            idade = maiorh
            nomevelho = nome
        else:
            if idade > maiorh:
                maiorh = idade
                nomevelho = nome
    if sexo == 'F':
        if idade <= 20:
            mulher20 += 1
    listidade.append(idade)
print('A media de idade do grupo é {}'.format(sum(listidade) / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 Anos. '.format(mulher20))