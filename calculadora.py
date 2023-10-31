#Função

rendaMensal = float(input('Insira sua renda mensual: R$: '))
emprestimoSolicitado = float(input('Insira o valor do emprestimo desejado: R$: '))
tempoDePago = int(input('Insira a quantidade de anos para pagar o emprestimo: '))
capacidadeMinimaPago = rendaMensal * 30 / 100
jurosMensais = emprestimoSolicitado * 0.97 / 100
meses = tempoDePago * 12
prestacaoMensalSemJuros = emprestimoSolicitado / (meses)
prestacaoMensalComJuros = prestacaoMensalSemJuros + jurosMensais
totalJuros = jurosMensais * meses
totalEmprestimo = emprestimoSolicitado + totalJuros

print('\n\nA sua capacidade maxima de pago mensal é de R$: {:.2f}'.format(capacidadeMinimaPago))
print('\n\nA taxa de juros é de (0.97%) Mensal \nValor dos juros mensais é de R$: {:.2f} \nValor das prestações mensais sem juros é de R$: {:.2f}'.format(jurosMensais, prestacaoMensalSemJuros))
print('\nValor total das prestações mensais com juros para {} anos é de R$: {:.2f}'.format(tempoDePago, prestacaoMensalComJuros))

if prestacaoMensalComJuros > capacidadeMinimaPago:
  print('\n\nAnalissando as informações inseridas, lamentamos informar \nque o credito devera ser negado, por quanto o valor das \nprestações mensais para o emprestimo solicitado é de R$: {:.2f}, \nultrapassando a sua capacidade maxima de pago mensal de R$: {:.2f}, \nfixada por os Bancos no (30%) do valor da renda mensal'.format(prestacaoMensalComJuros, capacidadeMinimaPago))
else:
  print('\nParabens, você cumpre com os requisitos para solicitar o emprestimo.')
  print('\nCredito Aprovado!')  
  print('\n\nO valor total dos juros para um emprestimo de {} anos é de R$: {:.2f} \nO valor total do emprestimo com os juros é de R$: {:.2f}'.format(tempoDePago, totalJuros, totalEmprestimo))
