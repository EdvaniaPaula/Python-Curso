sal = float(input('Qual o seu salario atual? R$'))
if sal <= 1250:
    new = sal + (sal * 15 / 100)
else:
    new = sal + (sal * 10 / 100)
print('Seu novo salário é R${:.2f}'.format(new))
