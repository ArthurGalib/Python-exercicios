n1 = float(input('nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2
print(f'A sua média é {media} ')
if media < 5:
    print('\033[0;31;40m REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('\033[0;33;40m RECUPERAÇÃO!')
elif media >= 7:
    print('\033[0;32;40m APROVADO! Parábens, continue assim.')