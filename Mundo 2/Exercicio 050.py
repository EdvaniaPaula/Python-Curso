# Desenvolva um programa que leia seis números inteiros e mostre a soma somente daqueles que forem pares. Se o valor digitado for impar desconsidere-o.
print('SOMATORIO DE PARES')
soma = 0
for i in range (0, 6):
  numero = int(input('Digite um número: '))
  if numero % 2 == 0 :
    soma += numero
print('Soma dos pares é igual a {} !'.format(soma))
