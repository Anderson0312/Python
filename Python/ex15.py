s = 0
cont = 0
for n in range(1, 501, 2):
    if n%3 == 0:
        s += n
        cont += 1
print('A soma de todos os {} valoresa solicitados é {}'.format(cont, s))