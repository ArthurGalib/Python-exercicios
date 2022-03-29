n = int(input('Digite um número qualquer: '))
e = int(input('''Você deseja escolher esse número para:
1) Binário
2) Octal
3) hexadecimal\n'''))
print('-=-'*20)
if e == 1:
    print(bin(n)[2:])
elif e == 2:
    print(oct(n)[2:])
elif e == 3:
    print(hex(n)[2:])
else:
    print('Escolha uma opção válida!')



