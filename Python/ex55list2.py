'''
teste = list()
teste.append('luis')
teste.append(22)
pessoas = list()
pessoas.append(teste[:])
teste[0] = 'maria' 
teste[1] = '21'
pessoas.append(teste[:])
print (pessoas)



galera = [['bruna', 22],['Anderson', 21],['lucia', 10],['mria', 45],['marcio',15],['luis', 50]]
for p in galera:
    print (f' {p[0]} tem {p[1]} anos de idade.')
'''  
    
todos = list()
dado = list()
totmaior = totmenor = 0
for i in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    todos.append(dado[:])
    dado.clear()
for pessoa in todos:
    if pessoa[1] >= 21:
        print (f' {pessoa[0]} tem {pessoa[1]} anos e é maior de idade.')
        totmaior += 1
    else:
        print (f' {pessoa[0]} tem {pessoa[1]} anos e é menor de idade.')
        totmenor += 1
print(f'temos {totmaior} maiores de idade e {totmenor} e menores de idade.')