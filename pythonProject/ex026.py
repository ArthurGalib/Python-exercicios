frase=str(input('Escreva uma frase: ')).upper()
print('Aparece a letra A {} vezes '.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima vez que ela aparece é na posição {}'.format(frase.rfind('A')+1))



