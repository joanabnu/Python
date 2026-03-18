palavras = ('aprender','Programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programar','futuro')

for p in palavras:
    print(f'Na palavra {p.upper()} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}' ,end=' ')