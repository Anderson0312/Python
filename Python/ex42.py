extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze'
           , 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('digite um número entre 0 e 20: '))
while num > 21:
    num = int(input('Tente novamente. digite um numeor entre 0 e 20: '))
    if num < 20:
        break
print(f'Você digitou o númeor {extenso[num]}.  ')
