from datetime import date
anoat = date.today().year
nasci = int(input('Digite sua data de nascimento: '))
idade = anoat - nasci
print('Sua idade é {} e de acordo com sua categoria voce é:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >= 15 and idade <= 19:
    print('JUNIOR')
elif idade >= 20 and idade <= 25:
    print('SêNIOR')
elif idade >= 26:
    print('MASTER')