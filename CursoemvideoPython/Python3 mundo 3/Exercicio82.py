lista = []
ListaPares = []
ListaImpa = []

while True: 
    n = int(input('Informe um numero : '))
    lista.append(n)
    contin = str(input('SIM/NÃO \nDigite se voce deseja continuar ')).upper().strip()

    if n % 2==0:
        ListaPares.append(n)
    else:
        ListaImpa.append(n)
    if contin == 'N':
        break

print(f'LISTA NORMAL : {lista} \nLista Pares : {ListaPares} \nLista Impa {ListaImpa}')