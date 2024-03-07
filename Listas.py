'''
PSI - Mod 5
Listas

'''

#Declarar lista
lista=['Pera','Cereja',1000,True]

print(lista)

#mostrar elemntos da lista um a um
for i in lista:
    print(i)

#mostar o elemento de uma dada posição
print('Elemento guardado na posição 2: ',lista[2])

#inceriri um elemento na ultima posição da lista
lista.append("Melão")

#inserir um elemento  numa determinada posição
lista.insert(2,'Melão')

#retirar o ultimo elemento da lista
lista.pop(0)
lista.pop()
#retirar um elemento especifico
lista.remove('Melão')

#apagar todos os elementos da lista
lista.clear()

#add uma lista de elemetos
lista.extend(['Banana','Manga','Lixia'])

#procurar elementos na lista
print(lista.index('Banana'))

#contar o elementos que tem um dado valor
print(lista.count('Manga'))

# ordenar uma lista
lista.sort()

#trocar a ordem dos elementos
lista.reverse()

#metodos para usar com listas numericas
lista_numerica=[1,2,3,4,5,6,7]

#Somar os elementos da lista
print(sum(lista_numerica))

#mostrar o maior valor
print(max(lista_numerica))

# mostrar o menor valor
print(min(lista_numerica))

#mostrar o nº de elementos que tem a lista
print(len(lista_numerica))



print(lista)