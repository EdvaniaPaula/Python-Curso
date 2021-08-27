from math import hypot
b = float(input('Valor do cateto oposto: '))
c = float(input('Valor do cateto adjacente: '))
h = hypot(b,c)
print('O comprimento da hipotenusa é igual a {:.1f}!'.format(h))
