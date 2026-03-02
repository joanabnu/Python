print('-=-' * 20) 
print('Analisandor de triangulo ')
print('-=-' * 20)
r1 = float(input('Primeiro segmento : '))
r2 = float(input('Segunda segmento : '))
r3 = float(input('Terceiro segmento : '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Primeiro : {} \nSegundo : {} \nTerceiro : {}\nOs segmentos acima podem forma triangulo! '.format(r1,r2,r3))
else: 
    print('Primeiro : {} \nSegundo : {} \nTerceiro : {} \nos segmentos acima nao podem forma um triangulo'.format(r1,r2,r3))