nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    print('O aluno teve a média {:.2f} e foi REPROVADO.'.format(media))
elif media >= 5 and media <= 6.9:
    print('O aluno teve a média {:.2f} e está de RECUPERAÇÃO.'.format(media))
elif media >= 7:
    print('O aluno teve a média {:.2f} e foi APROVADO.'.format(media))