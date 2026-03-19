num = list()
while True:
    n = int(input('Digite um valor : '))
    
    if n not in num:
        num.append(n)
        print('Valor adicionado!! ')
    else: 
        print('Valor duplicado ')
    contin = str(input('SIM/Não\nGostaria de continua : ')).upper().strip()
    if contin == 'N':
        break
print(f'O valores : {num} ')
num.sort()
print(f'Ordem crescente {num}')