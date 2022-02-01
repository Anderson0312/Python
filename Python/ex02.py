print('Banco AndersonEmpréstimos')
vahs = int(input('What is the valuer of the house ? R$ '))
wage = float(input('Who much do you get the wage? R$ '))
old = int(input('how old do you want to pay ? '))
prestaçao = vahs / (old * 12)  # para saber a quantidade de meses e a parcela da casa
minimo = (30 / 100) * wage # para saber quanto é 30% do salario da pessoa
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}.'.format(vahs, old, prestaçao))
if minimo > prestaçao:
    print('Seu emprestimo foi APROVADO!')
    print(
        'É necessario que a parcela não exceda 30$ do seu salario, seu salario calculado {:.2f}, prestação {:.2f}.'.format(
            minimo, prestaçao))
else:
    print('Seu emprestimo foi NEGADO!')
    print(
        'É necessario que a parcela não exceda 30$ do seu salario, seu salario calculado {:.2f}, prestação {:.2f}.'.format(
            minimo, prestaçao))

