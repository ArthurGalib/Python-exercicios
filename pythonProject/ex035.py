print('-=' * 30)
print('\033[0;31;40m]Analisador de triângulos °---° ')
print('-=' * 30)
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIÂNGULO! ')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
print('-=' * 0)
