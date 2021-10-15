


valorCasa = float(input('Qual o valor da casa? R$'))
SalarioP = float(input('Qual o valor do seu salario? R$'))
anos = int(input('Quantos anos de pagamento? '))
prestação = SalarioP * 30 / 100
mensal = anos * 12
if valorCasa / mensal <= prestação:
    print("Seu empréstimo foi aceito com sucesso! \nMáximo que você pode pagar por mês: R${:.2f} \nValor das "
          "prestações: R${:.2f}".format(prestação, valorCasa / mensal))
else:
    print("Empréstimo negado! \nMáximo que você pode pagar: R${:.2f} \nValor das prestações: R${:.2f}".format(prestação, valorCasa / mensal))
