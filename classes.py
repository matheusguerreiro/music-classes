listaAlunos = []
file = open('alunos.txt', 'a')
class aluno:
    def __init__(self, nome, idade, contato, instrumento, totaldeaulas, aulasporfazer):
        self.nome = nome
        self.idade = idade
        self.contato = contato
        self.instrumento = instrumento
        self.totaldeaulas = totaldeaulas
        self.aulasporfazer = aulasporfazer

def comprarAulas():
    print(f'{"cod":^5}{"nome":^32}')
    for c in range(0, len(listaAlunos)):
        print(f'{c:^5}{listaAlunos[c].nome:^32}')
    print(f'{"-" * 37}')
    c = int(input('cod: '))
    print(f'Aulas por Fazer: {listaAlunos[c].aulasporfazer}')
    qa = int(input('Quantidade de Aulas que vai Comprar: '))
    listaAlunos[c].aulasporfazer += qa
    listaAlunos[c].totaldeaulas += qa

def fazerAula():
    print(f'{"cod":5}{"nome":32}')
    for c in range(0, len(listaAlunos)):
        print(f'{c:^5}{listaAlunos[c].nome:^32}')
    print(f'{"-"*37}')
    c = int(input('cod: '))
    if listaAlunos[c].aulasporfazer == 0:
        print('\033[0;31mErro!\033[m\033[0;33mNão tem Aula por Fazer.\033[m')
    else:
        listaAlunos[c].aulasporfazer -= 1
        print('\033[0;32mAula Feita!\033[m')

def cadastrarAluno():
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    contato = str(input('Contato: ')).strip()
    instrumento = str(input('Instrumento: ')).strip().title()
    a = aluno(nome, idade, contato, instrumento, totaldeaulas=0, aulasporfazer=0)
    listaAlunos.append(a)

def statusdoAluno():
    print(f'{"cod":^5}{"nome":^32}')
    print(f'{"-"*37}')
    for c in range(0, len(listaAlunos)):
        print(f'{c:^5}{listaAlunos[c].nome:^32}')
    print(f'{"-"*37}')
    c = int(input('cod: '))
    print(f'{"Aluno: "}{listaAlunos[c].nome}\n'
          f'{"Idade: "}{listaAlunos[c].idade}\n'
          f'{"Contato: "}{listaAlunos[c].contato}\n'
          f'{"Instrumento: "}{listaAlunos[c].instrumento}\n'
          f'{"Aulas por Fazer: "}{listaAlunos[c].aulasporfazer}\n'
          f'{"Total de Aulas: "}{listaAlunos[c].totaldeaulas}')