# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for i in range (1, 500+1):
  if i % 2 == 1 and i % 3 == 0:
    s += i
    print(i)
print('A soma dos valores é igual a {}'.format(s))