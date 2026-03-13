n = cont = s = 0
while True:
    n = int(input('Digite um valor : '))
    if n == 999:
        break
    cont +=1
    s += n
print(f'A soma  : {s}')