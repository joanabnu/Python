lanche = ('Hamburguer','Suco','Pizza', 'Pudim')
# Tuplas são imutaveis
print(lanche[1])
print(lanche[-2:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range (0,len(lanche)):
    print(f'{lanche[cont]} na posicao {cont}')
print('Comi pra caramba')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')