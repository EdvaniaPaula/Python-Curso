valorProduto = float(input('Qual valor do produto? '))
print('Escolha seu tipo de pagamento abaixo:')
print('[ 1 ] Pagamento à vista dinheiro/cheque (10% de desconto)')
print('[ 2 ] Pagamento à vista no cartão (5% de desconto)')
print('[ 3 ] Pagamento em até 2x no cartão (preço normal)')
print('[ 4 ] Pagamento de 3x ou mais no cartão (20% de juros)')
escolha = int(input('Digite o numero escolhido: '))

if escolha == 1:
  new = valorProduto - (valorProduto * 10 / 100)
  print('Seu produto passa a valer R${} '.format(new))
elif escolha == 2:
  new = valorProduto - (valorProduto * 5 / 100)
  print('Seu produto passa a valer R${} '.format(new))
elif escolha == 3:
  print('Seu produto passa a valer R${} '.format(valorProduto))
elif escolha == 4:
  new = valorProduto + (valorProduto * 20 / 100)
  print('Seu produto passa a valer R${} '.format(new))
else:
  print("comando inválido")
