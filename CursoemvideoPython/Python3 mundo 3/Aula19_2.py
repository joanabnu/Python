estado = dict()
brasil = list()

for c in range(0, 3):
    estado['nome'] = str(input('Nome do Estado: '))
    estado['uf'] = str(input('Sigla (UF): '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo : {k}  tem o valor :  {v}', end=' ')