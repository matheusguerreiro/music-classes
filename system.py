import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="mgf",
    password="password"
)
mycursor = mydb.cursor()
mycursor.execute()
from classes import *
print(f'{"#"}'*50)
print(f'{" - AULAS DE MÚSICA - ":^50}')
print(f'{" - - - sistema - - - ":^50}')
print(f'{"#"}'*50)
print(f'{" - (1) - Cadastrar Aluno(a) - ":^50}')
print(f'{" - (2) - Status do Aluno(a) - ":^50}')
print(f'{" - (3) - Comprar Aulas - ":^50}')
print(f'{" - (4) - Sair - ":^50}')
print(f'{"#"}'*50)
while True:
    opcao = int(input('Opção: '))
    if opcao == 1:
        cadastrarAluno()
    elif opcao == 2:
        statusdoAluno()
    elif opcao == 3:
        comprarAulas()
    elif opcao == 4:
        print('Saindo...')
        break
    else:
        print('Erro! Opção Inválida.')
