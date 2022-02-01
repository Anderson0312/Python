listTime = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corintians',
            'RB Bragantino', 'Fluminense', 'Ameriaca-MG', 'Atletico-GO', 'Santos',
            'Ceará', 'Internacionla', 'São Paulo', 'Athletico=PR', 'Cuiaba')
print(listTime)
print('-=' * 20)
print(f'Os 5 Primeiros colocados são: {listTime[0:5]}')
print('-=' * 20)
print(f'Os ultimos 4 times são: {listTime[-4:]}')
print('-=' * 20)
print(f'OS times em Ordem alfabetica são: {sorted(listTime)}')
print('-=' * 20)
print(f'O time Flamengo se encontra na posição {listTime.index("Flamengo")+1}ª.')