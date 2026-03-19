num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
num
# num.sort(reverse=True)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o numero 5')
num.insert(2,2)
num.pop() 
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores): 
    print(f' Na posicao {c} encontrei o valor {v}...')

print('Cheguei ao final da lista.')

valoresLista = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor : ')))

for c,v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

a = [2,3,4,7]
b = a
# b = a[:] CRIA UMA COPIA DE A DENTRO DE B 
b[2] = 8
print(f'Lista A : {a}')
print(f'Lista B : {b}')