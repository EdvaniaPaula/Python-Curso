# Faça um algoritmo que leia o salário de funcionário e mostre seu novo salário, com 15% de aumento.


nome = input('Nome do funcionario: ')
sal = float(input('Salario atual: '))
new = sal + (sal * 15 / 100)
print('Olá {}, com 15% de aumento, seu novo salario é de R${:.2f}.'.format(nome, new))
