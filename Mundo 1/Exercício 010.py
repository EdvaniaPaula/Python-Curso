# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

# Considere o valor do dolar atual


real = float(input('digite o valor em real R$'))
dolar = real / 5.06
print('o valor de R${:.2f} é igual a {:.2f} dolares'.format(real, dolar))