nome=str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {} '.format(nome.upper()))
print('Seu nome com todas as lestras minúsculas: {} '.format(nome.lower()))
print('O seu nome tem {} letras. '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))




