lanche = ('Hamburguer','Suco','Pizza', 'Pudim')
# Tuplas são imutaveis
print(lanche[1])
print(lanche[-2:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('=='* 20)
for cont in range (0,len(lanche)):
    print(f'{lanche[cont]} na posicao {cont}')
print('Comi pra caramba')
print('==' * 20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('=='*20)
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c.count(5))
print(c.index(5,1))