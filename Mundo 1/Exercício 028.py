from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar escolhendo um numero.
print('\033[32;40m-=--\033[m'*19)
print('\033[32;40m O COMPUTADOR PENSOU UM UM NÚMERO DE 0 A 5, TENTE ACERTAR QUAL FOI O NUMERO!\033[m')
print('\033[32;40m-=--\033[m'*19)
escolhido = int(input('Digite um número de 0 a 5: '))
print('\033[1;32mprocessando...\033[m')
sleep(2)  #o sleep faz o programa parar por um tempo determinado
if escolhido == computador:
    print('\033[30;107m Você venceu! acertou é o numero {}!\033[m'.format(computador))
else:
    print('\033[97mNão é esse número, você errou! é o numero\033[m \033[97;42m {}!\033[m'.format(computador))
