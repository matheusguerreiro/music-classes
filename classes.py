listaAlunos = []
class aluno:
    def __init__(self, nome, idade, contato, instrumento, totaldeaulas, aulasporfazer, quantidadedeaulas):
        self.nome = nome
        self.idade = idade
        self.contato = contato
        self.instrumento = instrumento
        self.totaldeaulas = totaldeaulas
        self.aulasporfazer = aulasporfazer
        self.quantidadedeaulas = quantidadedeaulas

def comprarAulas():
    print(f'{"cod":^5}{"nome":^32}')
    for c in range(0, len(listaAlunos)):
        print(f'{c:^5}{listaAlunos[c].nome:^32}')
    c = int(input('cod: '))
    print(f'Aulas por Fazer: {listaAlunos[c].aulasporfazer}')
    qa = int(input('Quantidade de Aulas que vai Comprar: '))
    af = int(input('Aulas Feitas: '))
    listaAlunos[c].totaldeaulas += qa
    listaAlunos[c].aulasporfazer = qa - af

def cadastrarAluno():
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    contato = str(input('Contato: ')).strip()
    instrumento = str(input('Instrumento: ')).strip().title()
    a = aluno(nome, idade, contato, instrumento, totaldeaulas=0, aulasporfazer=0, quantidadedeaulas=0)
    listaAlunos.append(a)

def statusdoAluno():
    print(f'{"cod":^5}{"nome":^32}')
    print(f'{"-":37}')
    for c in range(0, len(listaAlunos)):
        print(f'{c:^5}{listaAlunos[c].nome:^32}')
    print(f'{"-":37}')
    c = int(input('cod: '))
    print(f'{"Aluno: "}{listaAlunos[c].nome}\n'
          f'{"Idade: "}{listaAlunos[c].idade}\n'
          f'{"Contato: "}{listaAlunos[c].contato}\n'
          f'{"Instrumento: "}{listaAlunos[c].instrumento}\n'
          f'{"Aulas por Fazer: "}{listaAlunos[c].aulasporfazer}\n'
          f'{"Total de Aulas: "}{listaAlunos[c].totaldeaulas}')