from datetime import date
print('Serviço militar obrigatório')
anonas = int(input('Digite seu ano de nascimento:'))
anoat = date.today().year
idade = anoat - anonas
print('Quem nasceu em {} tem  {} anos em {}.'.format(anonas, idade, anoat))
if idade < 18:
    saldo = 18 - idade
    print('Você tem {} ainda não esta na idade de alista, falta {} anos.'.format(idade, saldo))
elif idade == 18:
    print('Você tem 18 anos está na idade de se alistar, procure a junta militar mais proxima.')
elif idade > 18:
    saldo = idade - 18
    print('Você tem {} já, passou {} anos do seu alistamento. Vá a junta militar o mais possível.'.format(idade, saldo))