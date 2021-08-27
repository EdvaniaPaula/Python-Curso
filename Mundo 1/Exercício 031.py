distancia = float(input('Qua a distancia da viagem em Km? '))
if distancia <= 200:
    preço = distancia * 0.5
    print('Com a viagem de {:.0f}Km, o preço da passagem ficou por R${:.2f}'.format(distancia, preço))
else:
    print('Com a viagem de {:.0f}Km, o preço da passagem ficou por R${:.2f}'.format(distancia, distancia * 0.45))
