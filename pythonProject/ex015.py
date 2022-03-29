k = float(input('Informe a Km percorrida pelo carro: '))
qd = int(input('Informe a quantidade de dias alugados: '))
pa = (qd * 60) + (k * 0.15)
print('A Kilometragem percorrida foi de {:.2f}Km e o total de dias alugados foi de {} dias. Sabendo isso, o total do valor a ser pago é de R${:.2f} '.format(k, qd, pa))


