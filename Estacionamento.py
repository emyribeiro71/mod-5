Matriculas=[]

def menu():
    print("1- Entrada")
    print("2- Saida")


opcao=-1
carros =0
while opcao!=0:
    menu
    if opcao=='1': #Entrada
        Matriculas.append(input(''))
        
    elif opcao=='2':
        Matricula=input('')
        Matriculas.remove(Matricula)
        
    elif len(Matriculas)==5:
        print('Lotação excedida. Procure outro estacionamento!')
        break
    
'''
'''
PSI-M05
Simular um parque de estacionamento como o do palacio um programa com duas opções entrada e saida
se a pesso dizer para entrar ou sair guarda mos a matricula. 5 máximo
'''
def menu():
    print('=' * 30)
    print('ESTACIONAMENTO')
    print('=' * 30)
    print('1 - Entrar no estacionamento')
    print('2 - Sair do estacionamento')
    print('3 - Ver carros')
    print('0 - Sair do programa')
    print('=' * 30)
 
opcao=5
listaEstacionamento = []
while opcao!=0:
    menu()
    opcao=int(input('Digite sua opção: '))
    if len(listaEstacionamento) == 5:
        print('Sem lugares')
    elif opcao == 0:
        break
    elif opcao == 1:
        matricula = (input('Digite a matricula: '))
        listaEstacionamento.append(matricula)
    elif opcao == 2:
        matricula = (input('Digite a matricula: '))
        listaEstacionamento.remove(matricula)
    elif opcao == 3:
        print('\n----------------\nLista de carros:\n----------------')
        for nome in listaEstacionamento:
            print(f'{nome}')
        input('\nPressione enter para continuar...\n')
'''



