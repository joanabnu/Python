nome = str(input('Qual é seu nome : '))
if nome == 'Joana':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um Bom dia, {}'.format(nome))