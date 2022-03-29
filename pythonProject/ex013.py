s = float(input('Informe o seu salário: R$'))
ns = s + (s * 15 / 100)
print('O seu salário é de R${:.2f}, com o aumento de 15% ele passará a ser de R${:.2f}. '.format(s,ns))
