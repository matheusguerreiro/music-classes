from classes import *
print(f'{"#"}'*30)
print(f'{" - AULAS DE MÚSICA - ":^30}')
print(f'{" - - - sistema - - - ":^30}')
print(f'{"#"}'*30)
print(f'{" - (1) - Cadastrar Aluno(a) - ":^30}')
print(f'{" - (2) - Status do Aluno(a) - ":^30}')
print(f'{" - (3) - Comprar Aulas - ":^30}')
print(f'{" - (4) - Fazer Aula - ":^30}')
print(f'{" - (5) - Sair - ":^30}')
print(f'{"#"}'*30)
while True:
    opcao = int(input('Opção: '))
    if opcao == 1:
        cadastrarAluno()
    elif opcao == 2:
        if len(listaAlunos) == 0:
            print('\033[0;31mErro!\033[m\033[0;33mNenhum Aluno cadastrado.\033[m')
        else:
            statusdoAluno()
    elif opcao == 3:
        if len(listaAlunos) == 0:
            print('\033[0;31mErro!\033[m\033[0;33mNenhum Aluno cadastrado.\033[m')
        else:
            comprarAulas()
    elif opcao == 4:
        if len(listaAlunos) == 0:
            print('\033[0;31mErro!\033[m\033[0;33mNenhum Aluno cadastrado.\033[m')
        else:
            fazerAula()
    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('\033[0;31mErro! Presta Atenção Tchê.\033[m')
