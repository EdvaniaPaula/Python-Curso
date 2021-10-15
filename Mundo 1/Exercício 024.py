# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".



cidade = input('Digite o nome da cidade: ').strip()
print('Sua cidade começa com Santo? {}'.format('santo' in cidade[:5].lower()))
