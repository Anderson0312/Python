peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal. ')
elif imc >= 25 and imc <= 30:
    print('Você está sobrepeso.')
elif 30 >= imc <= 40:
    print('Você está obeso.')
else:
    print('Você está em obesidade mórbida.')