# Faça um programa que leia uma temperatura digitada em °C e converta para °F.


c = float(input('Qual a temperatura em °C? '))
f = (c * 9) / 5 + 32
print('A temperatura em {}°C, corresponde a {}°F.'.format(c, f))
