from random import randint
computador = randint(0,10)
tentativas = 0
print('O computador pensou em numero entre 0 e 10\nVoce conseguir adivinha !! ')
palpite = int(input('Qual é o palpite : '))

while computador != palpite:
    palpite = int(input('Tente novamente \nQual é o palpite : '))
    tentativas +=1
print('Paraben voce acertou!! \nApos a quantidade de tentativas : {} \nNumero do compuatador : {}'.format(tentativas,computador))