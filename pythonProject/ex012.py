p = float(input('Preço do produto: R$'))
np = p * 5 / 100
vf = p - np
print('O preço do produto é de {} Reais. Mas com o desconto de 5% ficará {} Reais'.format(p, vf))
