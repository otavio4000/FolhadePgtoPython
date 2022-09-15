from re import I
import uuid
 
LISTA_PROJETOS = []
LISTA_PROFISSIONAIS = []
 
class Profissional():
    def __init__(self, nome, valor, vigencia):
        self.id = uuid.uuid4()
        self.nome = nome
        self.bolsa = valor
        self.vigencia = vigencia
 
class Projeto():
 
    def __init__(self, nome, descricao, dataini, datafim, coord):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.dataini = dataini
        self.datafim = datafim
        self.coord = coord
        self.profissionais = []
        self.atividades = []
        self.status = 'Em processo de criação'
 
class Atividade():
 
    def __init__(self, nome, descricao, dataini, datafim, responsavel, atividadecont):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.dataini = dataini
        self.datafim = datafim
        self.resp = responsavel
        self.profissionais = []
        self.tarefas = []
 
def cadastrar_projeto():
    nome = input('Qual o nome do projeto?')
    descricao = (input('Qual a descrição do projeto?'))
    dataini = input('Qual a data inicial do projeto? Ex: 24/12/18 13:55:26 ')
    datafim = input('Qual a data final do projeto? Ex: 25/12/18 13:55:26 ')
    coord = input('Qual o nome do coordenador responsável pelo Projeto?')
    proj = Projeto(nome, descricao, dataini, datafim, coord)
    proj.nome = 'Outro nome'
    print(f'Projeto criado com sucesso! Salve o id do projeto:{proj.id}')
    LISTA_PROJETOS.append(proj)
 
def cadastrar_usuario():
    if len(LISTA_PROJETOS) == 0:
        print("Não é possível cadastrar usuário, não existem projetos no sistema. Por favor, crie um projeto")
        return
 
    nome = input('Qual o nome do Profissional?')
    valor = float((input('Qual o valor da bolsa?')))
    vigencia = (input('Qual o período de vigência da bolsa?'))
    user = Profissional(nome, valor, vigencia)
 
    print('Escolha o Projeto no qual este profissional pertence')
 
    for i in range(len(LISTA_PROJETOS)):
        print(f'[{i}] - {LISTA_PROJETOS[i].nome}')     
 
    escolha = int(input('Escolha: '))
 
    LISTA_PROJETOS[escolha].profissionais.append(user)
 
    print(f'Profissional criado com sucesso! Id do profissional:{user.id}')
 
 
def cadastrar_atividade():
    if len(LISTA_PROJETOS) == 0:
        print("Não é possível cadastrar uma atividade, não existem projetos no sistema. Por favor, crie um projeto")
        return
 
    nome = input('Qual a descrição da Atividade?')
    dataini = input('Qual a data inicial do projeto? Ex: 24/12/18 13:55:26 ')
    datafim = input('Qual a data final do projeto? Ex: 25/12/18 13:55:26 ')
    resp = input('Digite o nome do responsável')
    atv = Atividade(nome, dataini, datafim, resp)
 
    print('Escolha o Projeto no qual esta atividade pertence')
 
    for i in range(len(LISTA_PROJETOS)):
        print(f'[{i}] - {LISTA_PROJETOS[i].nome}')     
 
    escolha = int(input('Escolha: '))
 
    LISTA_PROJETOS[escolha].atividades.append(atv)
 
    print(f'Atividade criada com sucesso! Id da atividade:{atv.id}')
 
 
def consultar_projetos():
    print('Escolha o Projeto no qual você quer consultar')
 
    for i in range(len(LISTA_PROJETOS)):
        print(f'[{i}] - {LISTA_PROJETOS[i].nome}')     
 
    escolha = int(input('Escolha: '))
    projeto = LISTA_PROJETOS[escolha]
 
    print('Aqui estão as informações deste projeto:')
    print(f'{projeto.nome}\n{projeto.descricao}')
 
    for atividade in projeto.atividades:
        print(atividade.nome)
        print(atividade.descricao)
 
    for prof in projeto.profissionais:
        print(prof.nome)
        print(prof.descricao)
 
def remover_da_lista():
    nome = input('Digite o nome que você quer remover')
    index = -1
    for i in range(len(LISTA_PROJETOS)):
        if LISTA_PROJETOS[i].nome == nome:
            index = i
 
    if index != -1:
        LISTA_PROJETOS.pop(index)

def sistemadepagamento():
    nome = input('Informe o projeto no qual você deseja gerar a folha de pagamento.')
    index = -1
    projeto = LISTA_PROJETOS[index]
    for i in range(len(LISTA_PROJETOS)):
        if LISTA_PROJETOS[i].nome == nome:
            index = i
    
    if index != -1:
        print(f'{projeto.nome} - {projeto.valor}\n')

def mudarstatus():
    nome = input('Informe o nome do projeto no qual você deseja alterar os status.')
    index = -1
    projeto = LISTA_PROJETOS[index]
    for i in range(len(LISTA_PROJETOS)):
        if LISTA_PROJETOS[i].nome == nome:
            index = i 

    if len(projeto.atividades) > 0:
        if projeto.status ==  'Em processo de criação':
            projeto.status == 'Iniciado'
            print(f'O Status do projeto foi alterado para = {projeto.status}')
            return
        if projeto.status == 'Iniciado':
            projeto.status == 'Em andamento'
            print(f'O Status do projeto foi alterado para = {projeto.status}')
            return
        if projeto.status == 'Em andamento':
            projeto.status == 'Concluido'
            print(f'O Status do projeto foi alterado para = {projeto.status}')
            return
    else:
        {
            print('Não existem atividades vigentes nesse projeto.\nLogo não é possível alterar seus status.')
        }

        
def menu():
    print('Bem vindo ao sistema gerenciador de projetos')
    while True:
        print('O que você quer saber sobre o projeto?')
        print('[0] - Cadastre um novo projeto')
        print('[1] - Cadastre um novo usuário')
        print('[2] - Cadastre um nova atividade')
        print('[3] - Excluir um projeto.')
        print('[4] - Imprimir a folha de pagamento de um Projeto.')
        print('[5] - Alterar os status de um Projeto.')
        print('[99] - Sair')
        opt = int(input('Escolha sua opção'))
 
        if opt == 0:
            cadastrar_projeto()
            print(LISTA_PROJETOS[0].descricao)
        if opt == 1:
            cadastrar_usuario()
        elif opt == 2:
            cadastrar_atividade()
        elif opt == 3:
            remover_da_lista()
        elif opt == 4:
            sistemadepagamento()
        elif opt ==5:
            mudarstatus();
        elif opt == 99:
            break
 
 
if __name__ == '__main__':
    menu()
