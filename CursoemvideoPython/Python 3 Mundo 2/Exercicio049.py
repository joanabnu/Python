tabuada = int(input('Qual numero tabuada : '))
mult = 0
for c in range(0,11):
    mult = tabuada * c
    print('{} X {} = {}'.format(c,tabuada,mult))