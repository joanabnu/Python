ficha =[]
while True :
   
    nome = str(input('Nomes : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    contin = str(input('SIM / NÃO Gostaria de continua : ')).upper().strip()
    if contin == 'N':
        break
print('='*30)
print(ficha)
