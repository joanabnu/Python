def ficha(jog='Sem identificação',g=0):
    print(f'O jogador {jog} fez {g}')

nome = str(input('Nome do jogador : '))
gol = str(input('Numero de Gols : '))

if gol.isnumeric():
    gol = int(gol)
else: 
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else: 
    ficha(nome,gol)