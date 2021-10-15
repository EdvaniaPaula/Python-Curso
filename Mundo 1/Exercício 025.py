# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.



Nome = str(input('Qual o seu nome: ')).strip()
print('Seu nome tem Silva? {} '.format('silva' in Nome.lower()))
