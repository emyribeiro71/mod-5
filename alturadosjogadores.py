altura=list(map(int, input('Altura dos Jogadores: ').split() ))
npostes=0
for postes in altura:
    if postes>=190:
        npostes+=1

n_bases=0
for n_jogador in range(len(altura)):
    if n_jogador<=175:
        n_bases+=1


print(f'Media das alturas dos jogadores da equipa: {sum(altura)/len(altura):.1f}',)
print(f'Nº de bases: {n_bases}\nNº de Postes: {npostes}')


