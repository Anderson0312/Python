
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Bolo', 'batata frita')

# Se precisar da posição pode usar essa maneira usando o range, junto com o len.
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')

# Ou pode usar o enumerate abrindo antes o pos para dar a posição.
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posção {pos}')

# Maneira mais simple, usa se não precisar da posição.
for comida in lanche:
    print(f'Eu vou comer {comida}')


a = (2, 4, 6)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5)) # conta quantos 5 tem na variavel {c}
print(c.index(8)) # mostra em qual posição está o 8


pessoa = ('Anderson', 21, 'M', 62.5)
del(pessoa)
print(pessoa[1])