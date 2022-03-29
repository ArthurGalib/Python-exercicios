import math
co=float(input('Comprimento do cateto oposto de um triângulo retângulo: '))
ca=float(input('Comprimento do cateto adjacente de um triângulo retângulo : '))
hi=math.hypot(co,ca)
#hi=(co**2+ca**2)**(1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

