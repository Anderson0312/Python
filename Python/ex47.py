frase = ('aprender', 'programar', 'linguagem', 'python',
         'curos', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'futuro')
for p in frase:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')