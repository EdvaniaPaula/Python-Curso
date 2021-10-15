# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.



n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('o maior valor é o {}!'.format(maior))
print('o menor valor é o {}!'.format(menor))
