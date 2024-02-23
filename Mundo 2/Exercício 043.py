print('=== CALCULO IMC ===')
print('obs:ponha um (.) no lugar da virgula')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
print('calculando...')
imc= peso/altura**2
print("{:.2f}".format(imc))
if imc >= 18.5 and imc <= 25.0:
  print('Parabens! Peso ideal')
elif imc>3 and imc < 18.5:
  print('Você está Abaixo do peso')
elif imc > 25 and imc < 30:
  print('Sobrepeso')
elif imc >= 30 and imc <= 40:
  print('Obesidade')
elif imc > 40:
  print('Obesidade mórbida')
else:
  print('Erro! tente novamente')