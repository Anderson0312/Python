from datetime import date
contmaior = 0
contmenor = 0
for c in range(1, 8):
    anonas = int(input('Em que ano a {}º pessoa nasceu?'.format(c)))
    data = date.today().year
    idade = data - anonas
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(contmenor))
