from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
print('-=-' * 20)
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <=19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')

