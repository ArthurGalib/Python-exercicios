casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
print('Para Pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao < (salario*0.3):
    print('O seu empréstimo pode ser APROVADO!')
else:
    print('O seu empréstimo foi NEGADO! Pois, excedeu os 30% do seu salário mensal.')


