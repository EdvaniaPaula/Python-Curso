nome = str(input('Digite seu nome completo:'))
print('Em Maiúsculas: {}'.format(nome.upper()))
print('Em Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras sem contar os espaços: {} letras'.format(len(nome.replace(" ", ""))))
nome1 = nome.split()
print('Quantidade de letras do primeiro nome: {} letras'.format(len(nome1[0])))

