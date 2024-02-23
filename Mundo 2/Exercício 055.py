# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor.
maior = 0
menor = 0
print('Verificador de Pesos')
for i in range (1,6):
  peso = float(input('({}º) Peso: '.format(i)))
  
print('Menor peso: {} kilos'.format(menor))
print('Maior peso: {} kilos'.format(maior))