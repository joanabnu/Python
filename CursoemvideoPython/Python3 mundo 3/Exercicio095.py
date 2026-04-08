time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador : '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} Jogou ? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantas gols na partidas {c+1} ? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('--'*25)
for k,v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*30)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('='*40)
while True:
    busca = int(input('(999 para parar)Mostrar dados de qual jogador ? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador ')
    else:
        print(f'-- Levantamento do jogador com codigo {time[busca]['Nome']} : ')
        for i, g in enumerate(time[busca]['gols.']):
            print(f'No jogo {i+1} fez {g} gols.')
        print('='*40)
print('Volte sempre // Komme immer wieder')