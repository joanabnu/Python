jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador : '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} Jogou ? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantas gols na partidas {c} ? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('=-=' * 25)
print(jogador)
print('=-=' * 25)
for k,v in jogador.items():
    print(f'O campo {k} tem o {v}')
print('=-=' * 25)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f' = > Na partida {i+1} fez {v} Gols')
print(f'Foi o total {jogador["Total"]} Gols')