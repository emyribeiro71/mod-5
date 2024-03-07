pacientes=[]


#função para mostrar o menu
def menu():
    print("------ Menu Principal ------")
    print("\n1 - Admissão de paciente")
    print("\n2 - Atendimento ao paciente")
    print("\n3 - Paciente Urgente")
    print('\n4 - Listagem de Pacientes')
    print("\n5 - Anular consulta")
    print("\n6 - Pesquisar paciente")
    print("\n0 - Sair do Sistema")


opcao='-1'
while opcao != '0':
    menu()
    opcao = input('Digite a opção desejada: ')  

    #admissão de pacientes
    if opcao == "1":
        pacientes.append(input("Nome do paciente: "))

    #Listagem dos doentes
    elif opcao=='4':
        print('---------------------------------------\nLista de pacientes em espera:\n---------------------------------------')
        for nome in pacientes:
            print(nome)
        input('\n\nPressione ENTER para continuar...')

    elif opcao=="2":
        if len(pacientes)==0:
            print('Não existem mais pacientes na lista de espera.')
        else:
            print(pacientes[0], 'é chamado ao consultório')
            pacientes.pop[0]
            import time
            time.sleep(2) 
            print('Paciente atendido.')
    elif opcao=='3':
        nome=input('Nome do paciente urgente: ')
        pacientes.insert(0, nome)
        print('Paciente agendado como urgente.')
    elif opcao=='5':
        nome=input('Nome do Paciente: ')
        pacientes.remove(nome)
        print('Consulta anulada com sucesso!')
    elif opcao=='6':
        nome=input('Nome do paciente: ')
        if pacientes.count(nome)==0:
            print('Não existe niguem com esse nome na lista de espera.')
        else:
            print('O paciente está na posição ', pacientes.index(nome)+1)

    
    
    
    
    
    
    
    
    '''    
    elif opcao=='3':
        buscar_paciente = input('Insira o nome completo do paciente: ')
        posicao = pacientes.index(buscar_paciente)
        print(f'\nDados do {buscar_paciente}: \nNome: {pacientes[posicao]}')
    '''
    
    



