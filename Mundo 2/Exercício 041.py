# A confederação nacional de natação precisa de um  programa que leia o ano de nascimemto de um atleta e mostre sua categoria, de acordo com a idade: 
#   ->  Até 9 anos: MIRIM
#   ->  Até 14 anos: INFANTIL
#   ->  Até 19 anos: JUNIOR
#   ->  Até 20 anos: SÊNIOR
#   ->  Acima: MASTER


print('\033[32;40m          Confederação Nacional de Natação \033[m')
print('')
nascimento = int(input('Digite seu ano de nascimento: '))
ano = int(input('Em que ano estamos? '))
idade = ano - nascimento
print('')
print('\033[32;40mVeja abaixo sua categoria na natação!\033[m')
if idade > 0 and idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19: 
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria: SÊNIOR')
elif idade > 20: 
    print('Categoria: MASTER')
else:
    print('ERRO! COMANDO INVÁLIDO')
print('')