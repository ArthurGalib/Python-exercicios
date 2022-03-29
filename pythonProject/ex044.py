print('=' * 10, 'LOJA DE BOMBA DO GALIB', '=' * 10)
preço = float(input('Valor? R$ '))
print('''FORMAS DE PAGAMENTO
1) á  vista dinheiro/cheque
2) á vista cartão
3) 2x no cartão
4) 3x ou mais no cartão
Qual a opção desejada?\n''')
opção = int(input('Qual é a opção desejada? '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x ficando assim, R${parcela}')
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int('Quantas parcelas? ')
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS!')
print(f'Sua compra de R${preço} vai custar R${total} no final.')

