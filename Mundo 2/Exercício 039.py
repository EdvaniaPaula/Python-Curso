
nascimento = int(input('Informe o seu ano de nascimento: '))
idade = 2021 - nascimento
if idade == 18:
    print('=#=' * 30)
    print('Você está apto para se alistar com {} anos.'.format(idade))
    print('Ano de alistamento: {}'.format(2021 - (idade-18)))
elif idade > 18 :
    print('=#=' * 30)
    print('Não pode se alistar, seu prazo de alistamento está vencido')
    print('Ano de alistamento: {}'.format(2021 - (idade-18)))
    print('Vencido a {} ano(s) '.format(idade-18))
else:
    print('=#=' * 30)
    print('Você ainda vai se alistar!')
    print('Ano de alistamento: {}'.format(2021 + (18-idade)))
    print('Ainda falta {} ano(s) '.format(18-idade))
