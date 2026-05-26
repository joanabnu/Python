c = (
    '\033[m',         # sem cor
    '\033[0;30;41m',  # vermelho
    '\033[0;30;42m',  # verde
    '\033[0;30;43m'   # amarelo
)

print(f'{c[1]}VERMELHO{c[0]}')
print(f'{c[2]}VERDE{c[0]}')
print(f'{c[3]}AMARELO{c[0]}')
def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end=' ')
    
    print('~' * tam)
    print('f {msg}')
    print('~' * {msg})
    print(c[0],end=' ')
# Programa Principal 
comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)
titulo('Ate logo!',1)