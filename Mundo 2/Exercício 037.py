

numero = int(input('Digite um número inteiro: '))
print('''Escolha qual será a forma de conversão:
[ 1 ] para Binario (base 2) 
[ 2 ] para Octal (base 8)
[ 3 ] para Hexadecimal (base 16)''')
resposta = int(input('Sua resposta: '))
if resposta == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif resposta == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif resposta == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[1;31m[Comando inválido! tente novamente] \033[m')
