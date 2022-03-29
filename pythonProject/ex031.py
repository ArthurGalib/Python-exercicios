dist=float(input('Qual a distância da viagem? '))
print('A sua viagem é de {:.2f}Km. '.format(dist))
if dist <= 200:
    preb=dist*0.5
    print('O valor a ser pago será R${:.2f}'.format(preb))
else:
    prea=dist*0.45
    print('O valor a ser pago será R${:.2f}'.format(prea))

