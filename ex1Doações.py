doacoes=[]

while True:
    doacao=int(input('Valor da doação: '))
    if doacao==0:
        break
    else:
        doacoes.append(doacao)
print('Nº de doações: ', len(doacoes))
print('Valor acumudado em doações: ', sum(doacoes))