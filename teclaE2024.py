'''
PSI - MOD 5
TECLA E - 2024
'''

N=int(input("Nº de Mareinheiros: "))


Marinheiros=[]
for x in range(1, N+1):
    Marinheiros.append(x)

apagar=[]
while len(Marinheiros)!=1:
    print(Marinheiros)
    for i in range(len(Marinheiros)): 
        if i%2==0:
            apagar.append(Marinheiros[i])
    for i in apagar:
        Marinheiros.remove(i)
    apagar.clear()
print(Marinheiros)


