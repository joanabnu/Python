pessoa = list()
dado = list()
pessoaPesada = list()
pessoaLeve = list()
QuantPessoa = 1
quantPessoaPessada = 0
quantPessoaleve = 0
while True:
    dado.append(str(input('Informe o seu nome : ')))
    dado.append(int(input('Informe o seu peso : ')))
    pessoa.append(dado[:])
    dado.clear()
    QuantPessoa +=1
    contin = str(input('Sim / Não \nInforme se gostaria de continua : ')).upper().strip()
 
    if contin == 'N':
        break
print(pessoa)
print(f'Quantidade : {QuantPessoa}')
print('--'*20)
for p in pessoa:
    if p[1] >= 100:
        pessoaPesada.append(pessoa)
        print(f'A pessoa mais pessada {p[0]} \nQuantidade de pessoa acima do peso {p[1]}')
        quantPessoaPessada += 1
    else:
        pessoaLeve.append(pessoa)
       
        print(f'A pessoa mais leve é : {p[0]} \nQuantidade de pessoa acima do peso {p[1]} ')
        quantPessoaleve += 1
print('==' * 20)
print(f'Quantidade de pessoa pessada : {quantPessoaPessada}')
print(f'Quantidade de pessoa leve : {quantPessoaleve}')
