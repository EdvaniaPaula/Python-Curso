# Crie um programa que leia a duas notas de aluno e calcule sua média, mostrando uma menssagem no final de acordo com a média atingida:
#-> média abaixo de 5.0 : REPROVADO
#-> média entre 5.0 e 6.9 : RECUPERAÇÃO
#-> média 7.0 ou superior : AOROVADO


nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0 and media <= 10 :
    print('Média: {:.1f}  PARABÉNS VOCÊ ESTÁ APROVADO(A)!'.format(media))
elif media >= 5.0 and media <= 6.9 :
    print('Média: {:.1f}  VOCÊ ESTÁ EM RECUPERAÇÃO!'.format(media))
elif media < 5.0:
    print('Média: {:.1f}  SINTO MUITO VOCÊ ESTÁ REPROVADO(A)!'.format(media))
else:
    print('COMANDO INVÁLIDO!')