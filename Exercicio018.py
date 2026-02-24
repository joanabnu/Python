from math import radians, sin,cos,tan
angulo =  float(input('Digite o angulo que voce deseja : '))

seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2} '.format(angulo,seno))
cosseno =  cos(radians(angulo))
print('O angulo de {} te, cosseno de {:.2}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a Tangente de {:.2} '. format(angulo,tangente))