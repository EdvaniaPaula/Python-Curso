# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando um laço for.
n = int(input('Qual tabuada você deseja ver? '))
for i in range (0, 11):
  print('{} X {} = {}'.format(n, i, n * i))