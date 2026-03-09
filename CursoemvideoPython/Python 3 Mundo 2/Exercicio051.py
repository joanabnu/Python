primeiro = int(input('Primeiro termo : '))
razao = int(input('Razao : '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,10,razao):
    print('{}'.format(c), end=' - ')
print('Acabou')