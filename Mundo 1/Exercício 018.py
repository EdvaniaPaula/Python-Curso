import math
ângulo = float(input('Digite o ãngulo que você deseja: '))
sen = math.sin(math.radians(ângulo))
print('O ângulo de {}° tem o SENO de {:.2f} '.format(ângulo, sen))
cos = math.cos(math.radians(ângulo))
print('O ângulo de {}° tem o COSSENO de {:.2f} '.format(ângulo, cos))
tg = math.tan(math.radians(ângulo))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(ângulo, tg))
