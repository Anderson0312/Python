cont = soma = media = menor = 0
maior = 0
sn = ''
while sn in 'Ss':
    n = int(input('Digite um numero: '))
    sn = str(input('Quer continuar? [S/N]')).strip()[0]
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))