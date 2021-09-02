# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Acima de R$1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


sal = float(input('Qual o seu salario atual? R$'))
if sal <= 1250:
    new = sal + (sal * 15 / 100)
else:
    new = sal + (sal * 10 / 100)
print('Seu novo salário é R${:.2f}'.format(new))
