number = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converte para BINÁRIO')
print('[ 2 ] converte para OCTAL')
print('[ 3 ] converte para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO fica {}.'.format(number, bin(number)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL fica {}.'.format(number, oct(number)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL fica {}.'.format(number, hex(number)[2:]))
else:
    print('Opção invalida digite novamente. ')