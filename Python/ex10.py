print('{:=^40}'.format('LOJA ANDERSON'))
print('----------------------------------------')
conta = float(input('Digite o valor a ser pago: '))
print('Escolha uma das opcões abaixo, como forma de pagamento')
print('----------------------------------------')
print('[ 1 ] À vista dinheiro/cheque: 10% de desconto.')
print('[ 2 ] À vista no cartão: 5% de desconto.')
print('[ 3 ] Em até 2x no cartão: preço normal.')
print('[ 4 ] 3x ou mais no cartão: 20% de juros.')
opc = int(input('opção escolhida: '))
if opc == 1:
    desconto = conta - ((10 / 100) * conta)
    print('O valor final da sua conta com desconto de 10% é R${:.2}.'.format(desconto))
elif opc == 2:
    desconto = conta - ((5 / 100) * conta)
    print('O valor final da sua conta com desconto de 5% é R${:.2}.'.format(desconto))
elif opc == 3:
    print('O valor da conta final é o mesmo por ser 2x sem juros no cartão R${:.2}.'.format(conta))
elif opc == 4:
    juros = conta + ((20 / 100) * conta)
    parcelas = int(input('Quantas vezes você vai querer parcelar: '))
    qnt = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcelas, qnt))
    print('O valor final da sua conta com Juros de 10% é R${:.2f}.'.format(juros))
else:
    print('Digite novamente uma das opçoes validas. ')

