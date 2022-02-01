from random import randint
sortado = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(sortado)
print(f'O maior numero sorteado foi {max(sortado)}')
print(f'O menor numeor sorteado foi {min(sortado)}')