# Escreva um programa que leia um valor em metros e o exiba convertido em centímentros e milímetros.


m = float(input('Metros: '))
c = m * 100
ml = c * 10
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
print('valor de {} metros em :{}km'.format(m, km))
print('valor de {} metros em :{}hm'.format(m, hm))
print('valor de {} metros em :{}dam'.format(m, dam))
print('valor de {} metros em :{:.0f}dm'.format(m, dm))
print('valor de {} metros em :{:.0f}cm'.format(m, c))
print('valor de {} metros em :{:.0f}mm'.format(m, ml))
