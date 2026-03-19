num = list()
while True:
    num.append(int(input('Digite um valor : ')))
    contin= str(input('Gostaria de continua : ')).upper().strip()
    if contin == 'N':
        break
print(f'O valores : {num} \nNumeros ordem crescente {num.sort()}')