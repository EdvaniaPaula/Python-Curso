# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.



n = input ('Digite algo: ')
print('a classe/tipo:', type(n))
print('Só tem espaços', n.isspace())
print('É numerico?', n.isnumeric())
print('É alfabetico?',n.isalpha())
print('É alfanumerico?',n.isalnum())
print('Está em Maiúsculas?',n.isupper())
print('Está em minúsculas?',n.islower())
print('Está capitalizada?',n.istitle())
