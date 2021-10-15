# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.



from math import hypot
b = float(input('Valor do cateto oposto: '))
c = float(input('Valor do cateto adjacente: '))
h = hypot(b,c)
print('O comprimento da hipotenusa é igual a {:.1f}!'.format(h))
