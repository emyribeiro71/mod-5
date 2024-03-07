'''
simulador
Sorteio Euromilhões
'''
import random
numeros=[]
for i in range(51):
    numeros.append(i)
n_sorteados=[]
for j in range(5):
    numero=random.choice(numeros)
    n_sorteados.append(numero)
    numeros.remove(numero)

chave_escolhida=input('Escolha uma chave numerica: ')
if chave_escolhida==n_sorteados:
    print('Parabéns! Você acertou o número')
    print('Os números sorteados foram: ',n_sorteados)
elif chave_escolhida.find(): 
    print


