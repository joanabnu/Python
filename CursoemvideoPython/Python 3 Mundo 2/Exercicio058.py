from random import randint
computador = randint(0,10)
print('O computador pensou em numero entre 0 e 10\nVoce conseguir adivinha !! ')
palpite = int(input('Qual é o palpite : '))

while computador != palpite:
    palpite = int(input('Tente novamente \nQual é o palpite : '))
print('Paraben voce acertou!! \nNumero do compuatador : {}'.format(computador))