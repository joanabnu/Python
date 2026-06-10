import moeda

p = float(input('Digite o preco R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de  {p} é {moeda.dobro(p)}')
print(f'O diminuir de {p} é {moeda.dimunuir(p,10)}')
print(f'O aumentado de {p} é {moeda.aumentar(p,10)}')