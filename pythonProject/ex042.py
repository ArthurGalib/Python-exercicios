r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
print('-=-' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PODE formar um triângulo ', end = '')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('NÃO pode formar um triângulo')
print('-=-' * 20)
