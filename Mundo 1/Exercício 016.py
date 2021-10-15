# Crie um programa que leia um número Real qualquer no teclado e mostre na tela a sua porção inteira.


from math import trunc
n = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(n, trunc(n)))
