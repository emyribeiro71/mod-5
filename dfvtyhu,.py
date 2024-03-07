concorrentes=[ ]
N_Candidatos=input('Qual é o nº de candidatos: ')
for i in range(N_Candidatos):
    concorrentes.append(i+1)

for i in range(concorrentes+1):
    for c in concorrentes:
        if c % 2!=0:
            concorrentes.remove(c)