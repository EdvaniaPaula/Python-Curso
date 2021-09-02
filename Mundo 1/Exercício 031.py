# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando R$0.50 por km para viagens até 200 km e R$0.45 por viagens mais longas.


distancia = float(input('Qua a distancia da viagem em Km? '))
if distancia <= 200:
    preço = distancia * 0.5
    print('Com a viagem de {:.0f}Km, o preço da passagem ficou por R${:.2f}'.format(distancia, preço))
else:
    print('Com a viagem de {:.0f}Km, o preço da passagem ficou por R${:.2f}'.format(distancia, distancia * 0.45))
