'''
anagrama
'''
def nivel():
    print('~~~~~~~~~~~JOGO DAS PALAVRAS~~~~~~~~~~~')
    print('> Nivel 1')
    print('> Nivel 2')
    print('> Nivel 3')



import random
palavras=['abacaxi','banana','macaco', 'cachorro', 'Computador', 'Oculos','caderno','livro', 'Mesa', 'Agua','carteira','Faca','Otorrinolaringologista','Paralelepipedo']
string=random.choice(palavras)
palavras.remove(string)


#guardar a palavra letra a letra
palavra=[]
for letra in string:
    palavra.append(letra)

#repetir o jogo
    while True or len(palavras)!=0:
        
        #baralhar as letras
        while len(palavra)!=0:
            letra_escolhida= random.choice(palavra)
            print(letra_escolhida, end='')
            palavra.remove(letra_escolhida)
    tentativas=3
    while tentativas!=0:
        tentativa=input("Qual é a palavra: ").upper()
        if palavra==tentativa:
            print('Parabéns! Acertou a palavra')
            break
        else:
            print('Errou! Tente novamente')
            tentativas-=1
        if tentativas==0:
            print('Game Over!')
            break




