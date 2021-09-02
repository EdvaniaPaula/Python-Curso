# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


from datatime import data
ano = int(input('Digite o ano para a analise! Digite 0 para o ano atual: '))
if ano == 0:
    ano = data.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto! '.format(ano))
else:
    print('O ano {} NÃO é bissexto! '.format(ano))
