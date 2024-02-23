# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
for i in range (0,100):
  numero = int(input('Digite um número: '))
  if numero % 1 == 0 and numero % numero == 0:
    print('É primo')
  else:
    print('Não é primo')
print('FIM')
