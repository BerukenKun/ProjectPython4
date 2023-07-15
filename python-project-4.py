colaborador = {}   # inicia o dicionário
lista_colaboradores = []   # inicia a lista
id_global = 0   #id global iniciada com 0



print('Bem-vindo ao Controle de Colaboradores do Gabriel Peixoto de Campos')   # mensagem de boas-vindas



# função para cadastrar um colaborador
def cadastrar_colaborador(id):
    while True:
        try:
            print('')
            print('*' * 74)
            print('-' * 24 + 'MENU CADASTRAR COLABORADOR' + '-' * 24)

            print('id do colaborador {}'.format(id))   # mostra o id que o colaborador vai receber
            colaborador['id'] = id   # a variável colaborador (que é um dicionário) recebe o id
            colaborador['nome'] = input('Entre com o nome: ')   # a variável colaborador (que é um dicionário) recebe o nome
            colaborador['setor'] = input('Entre com o setor: ')   # a variável colaborador (que é um dicionário) recebe o setor
            colaborador['pagamento'] = float(input('Entre com o pagamento (R$): '))   # a variável colaborador (que é um dicionário) recebe o pagamento
            lista_colaboradores.append(colaborador.copy())   # adiciona os dicionários no final da lista

        except ValueError:   # caso o pegamento recebido for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar novamente
            print('\nVocê digitou um valor não numérico!')
            print('Por favor entre com a opção novamente.')
            continue

        else:
            break



# função para consultar os colaboradores
def consultar_colaborador():
    while True:
        try:
            print('')
            print('*' * 74)
            print('-' * 24 + 'MENU CONSULTAR COLABORADOR' + '-' * 24)

            print('Escolha a opção desejada')
            print('1 - Consultar todos os colaboradores')
            print('2 - Consultar colaborador por id')
            print('3 - Consultar colaborador(es) por setor')
            print('4 - Retornar')
            op = int(input('>'))   # recebe a opção digitada
            print('')

            if(op >= 1 and op <= 4):   # verifica se a opção é válida
                if(op == 1):   # se a opção for 1

                    print('-' * 30)

                    for e in lista_colaboradores:   # percorre a lista

                        for i,j in e.items():   # i é os "dicionários" e o j são os valores
                            print(i,':',j)   # mostra os colaboradores com os "dicionários"

                        print('-' * 30)

                elif(op == 2):   # se a opção for 2
                    id_colaborador = int(input('Digite o id do colaborador: '))   # recebe o id do colaborador que será analisado
                    print('')

                    print('-' * 30)

                    for e in lista_colaboradores:   # percorre a lista
                        if(e['id'] == id_colaborador):   # se o id do colaborador for igual ao id que foi digitado, então mostra o colaborador

                            for i, j in e.items():   # i é os "dicionários" e o j são os valores
                                print(i, ':', j)   # mostra os colaboradores com os "dicionários"

                            print('-' * 30)

                elif(op == 3):   # se a opção for 3
                    setor_colaborador = input('Digite o setor do(s) colaborador(es): ')   # recebe o setor do colaborador que será analisado
                    print('')

                    print('-' * 30)

                    for e in lista_colaboradores:   # percorre a lista
                        if(e['setor'] == setor_colaborador):   # se o setor do colaborador for igual ao setor que foi digitado, então mostra o colaborador

                            for i, j in e.items():   # i é os "dicionários" e o j são os valores
                                print(i, ':', j)   # mostra os colaboradores com os "dicionários"

                            print('-' * 30)

                else:   # se a opção for 4 (retornar), então volta para o menu
                    break

            else:  # se o valor informado não for 1, 2, 3 ou 4, será exibido a mensagem de erro abaixo e depois tentar adicionar a opção novamente
                print('\ndigite uma opção correta.')
                print('Por favor tente novamente')
                continue

        except ValueError:   # caso a opção recebida for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar novamente
            print('\nVocê digitou um valor não numérico!')
            print('Por favor entre com a opção novamente.')
            continue



# função para remover um colaborador
def remover_colaborador():
    while True:
        try:
            print('')
            print('*' * 74)
            print('-' * 24 + 'MENU REMOVER COLABORADOR' + '-' * 24)

            id_colaborador = int(input('Digite o id do colaborador a ser removido: '))   # recebe o id do colaborador que será excluído

            print('')

            for e in lista_colaboradores:   # i é os "dicionários" e o j são os valores
                if (e['id'] == id_colaborador):   # se o id do colaborador for igual ao id que foi digitado, então o colaborador será excluído
                    lista_colaboradores.remove(e)   # remove o colaborador

        except ValueError:   # caso a opção recebida for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar novamente
            print('\nVocê digitou um valor não numérico!')
            print('Por favor entre com a opção novamente.')
            continue

        else:   # volta para o menu depois de excluir um colaborador
            break




#   MAIN   #

while True:
    try:
        print('')
        print('*' * 74)
        print('-' * 30 + 'MENU PRINCIPAL' + '-' * 30)

        print('Escolha a opção desejada')
        print('1 - Cadastrar colaborador')
        print('2 - Consultar colaborador(es)')
        print('3 - Remover colaborador')
        print('4 - Sair')
        op = int(input('>'))   # recebe a opção digitada

        if(op >= 1 and op <= 4):   # verifica se a opção é válida
            if(op == 1):   # se a opção for 1
                id_global+=1
                cadastrar_colaborador(id_global)
            elif(op == 2):   # se a opção for 2
                consultar_colaborador()
            elif(op == 3):   # se a opção for 3
                remover_colaborador()
            else:   # se a opção for 4, encerra o programa
                break

        else:  # se o valor informado não for 1, 2, 3 ou 4, será exibido a mensagem de erro abaixo e depois tentar adicionar a opção novamente
            print('\ndigite uma opção correta.')
            print('Por favor tente novamente')
            continue

    except ValueError:   # caso a opção recebida for uma letra, mostrar a mensagem de erro abaixo, e depois perguntar novamente
        print('\nVocê digitou um valor não numérico!')
        print('Por favor entre com a opção novamente.')
        continue













































