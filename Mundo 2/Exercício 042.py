print('-=-'*20)
print('  ANALIZADOR DE TRIÂNGULOS  ')
print('-=-'*20)
n1 = float(input('Primeiro sigmento: '))
n2 = float(input('Segundo sigmento: '))
n3 = float(input('Terceiro sigmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É POSSIVEL formar um triângulo!')
    if n1 == n2 == n3 :
        print('triângulo EQUILÁTERO!')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('triângulo ISÓSCELES!')
    elif n1 != n2 != n3:
        print('triângulo ESCALENO!')
else:
    print('NÃO É POSSIVEL formar um triângulo!')
   