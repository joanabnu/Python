aluno = dict()
media = 0
aluno['nome'] = str(input('Informe o seu nome : '))
aluno['nota'] = float(input('Informe Nota :'))

if aluno['nota'] <= 6:
    aluno[media] = 'Reprovado'
else:
    aluno[media] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} = {v}')

