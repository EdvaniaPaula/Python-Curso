# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma messagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.


velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = velocidade - 80
    print('Você está multado por passar da velocidade permitida!')
    print('Multa de R${}'.format(multa * 7))
print('Tenha um Bom Dia! Você está na velocidade permitida.')
