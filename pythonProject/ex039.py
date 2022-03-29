from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem {} anos, vá se alistar')
elif idade < 18:
    saldo = 18 - idade
    print(f'Falta {saldo} anos para você se alistar. ')
else:
    saldo = idade - 18
    print(f'Você já DEVERIA TER SE ALISTADO! há {saldo} anos.')





