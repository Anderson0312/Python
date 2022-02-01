lado1 = int(input('Digite o tamanho do primeiro lado: '))
lado2 = int(input('Digite o tamanho do segundo lado: '))
lado3 = int(input('Digite o tamanho do terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM FORMAR UM TRIâNGULO!')
    if lado1 == lado2 == lado3:
        print('O triângulo formado é equilatero. ')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('O triângulo formado é isisceies. ')
    elif lado1 != lado2 != lado3 != lado1:
        print('O triângulo formado é escaleno. ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIâNGULO! ')
