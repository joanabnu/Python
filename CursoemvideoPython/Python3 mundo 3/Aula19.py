pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'Idade': 22}
del pessoa['sexo']
pessoa['nome'] = 'Leandro'
print( pessoa.keys())
print(pessoa.values())
print(pessoa.items())
for k, v in pessoa.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro ','sigla': 'RJ' }
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(f'Estado 1: {estado1} \nEstado 2: {estado2}')
print(brasil[1]['uf'])