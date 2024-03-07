'''
mod 5 - Listas
sorteio da Champion

'''
clubes=input('Insira a lista de clubes separados por uma virgula: \n'.split(','))

import random
n_jogos=1
while len(clubes)!=0:
    print(f'Jogo {n_jogos}: ')
    clube_sorteado=random.choice(clubes)
    print(clube_sorteado, " - ",end='')
    clubes.remove(clube_sorteado)

    clube_sorteado=random.choice(clubes)
    print(clube_sorteado, "\n")
    clubes.remove(clube_sorteado)

    n_jogos+=1

