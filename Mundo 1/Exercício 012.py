# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


valor = float(input('digite o valor do produto: R$'))
print('R${} com desconto de 5% fica igual a {:.2f}'.format(valor, valor * 0.95))
