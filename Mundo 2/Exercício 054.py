#  Crie um programa que leia o ano de nascimemto de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores
maior = 0
menor = 0
print('Verificador de MAIORIDADE')
for i in range (0,7):
  idade = int(input('Sua idade: '))
  if idade >= 18:
    maior += 1 
  else:
    menor += 1  
print('Total de {} pessoas na maioridade e {} menores de 18.'.format(maior, menor))