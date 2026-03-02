velocidade = float(input('Qual é a velocidade atual do carro : '))
if velocidade > 80:
   print('MULTADO!! Voce excedeu o limite permitido que é de 80km/h')
   multa = (velocidade-80) * 7
   print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
   print('Tenho um Bom dia, Dirija com segurança')