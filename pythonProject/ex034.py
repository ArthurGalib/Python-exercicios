salario=float(input('Qual o seu salário em R$? '))
print('O seu salário é de R${:.2f}'.format(salario))
if salario>1250:
    maior=(salario*0.1)+salario
    print('O seu salário passará a ser de R${:.2f}'.format(maior))
else:
    menor=(salario*0.15)+salario
    print('O salário passará a ser de R${:.f}'.format(menor))
