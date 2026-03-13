from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor : '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar ?')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!!')
            v += 1
        else:
            print('Voce Perdeu!!')
            break
    elif tipo == 'I':
     if total % 2 ==1:
        print('Voce Venceu!')
        v += 1
    else:
        print('Voce Perdeu')
        break
    print('Vamos jogar novamente')
print(f'Voce venceu {v}')
