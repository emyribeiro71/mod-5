NAtletas=int(input('Quantos atletas participam na prova? '))

lancamentos=[0]*NAtletas

for numero in range(NAtletas):
    lancamentos[numero]=int(input(f'Lançamento do atleta nº{numero+1}: '))
lancamentos.sort()
lancamentos.reverse()


print(f'O melhor lançamento foi {max(lancamentos)/100}m')
print(f'O vencedor é o atleta nº{lancamentos.index(max(lancamentos))+1}.')
print(f'Os 3 melhores lançamentos são: {lancamentos[:3]}')