a=int(input('Informe o primeiro número: '))
b=int(input('Informe o segundo número: '))
c=int(input('Informe o terceiro número: '))
#print('maior:',max(a,b,c))
#print('Menor: ',min(a,b,c))

#verificando quem é menor
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

#verificando quem é maior
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))



