from random import randint 
from time import sleep
itens = ('Pedro', 'Papel', 'Tesoura')
computador = randint(0,2)

print('Sua opcoes \n[0]Pedra \n[1]Papel \n[2]Tesoura')

jogador = int(input('Qual é sua jogada : '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('=='* 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=='*15)
# print('O computador escolheu {}'.format(itens[computador]))

if computador == 0:
    if jogador == 0:
        print('Empate')   
    elif jogador == 1:
         print('Joagador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogador invalido')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')   
    elif jogador == 1:
        print('Empate')   
    elif jogador == 2:
        print('Jogador vencer')   
    else:
         print('Jogador invalido')
elif computador == 2:
    if jogador == 0:
        print('Jogador vencer')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')   
    else: 
        print('Jogador invalido')