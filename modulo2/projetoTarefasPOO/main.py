from datetime import datetime

# -----------------------
# Classe Gestor
# -----------------------
class Gestor:
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)
        projeto.gestor = self

    def listar_projetos(self):
        print(f"\nProjetos gerenciados por {self.nome}:")
        if not self.projetos:
            print("Nenhum projeto cadastrado.")
        for i, projeto in enumerate(self.projetos, start=1):
            print(f"{i}. {projeto.nome}")

    def listar_todas_tarefas(self):
        print(f"\nTodas as tarefas sob gestão de {self.nome}:")
        if not self.projetos:
            print("Nenhum projeto encontrado.")
        for projeto in self.projetos:
            print(f"\nProjeto: {projeto.nome}")
            projeto.listar_tarefas()


# -----------------------
# Classe Projeto
# -----------------------
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
        self.gestor = None

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        tarefa.projeto = self

    def listar_tarefas(self):
        if not self.tarefas:
            print("  Nenhuma tarefa cadastrada.")
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"  {i}. {tarefa.nome} | Status: {tarefa.status} | Prioridade: {tarefa.prioridade} | Prazo: {tarefa.prazo}")


# -----------------------
# Classe Tarefa
# -----------------------
class Tarefa:
    def __init__(self, nome, descricao, prioridade="Média", prazo=None):
        self.nome = nome
        self.descricao = descricao
        self.status = "Pendente"
        self.projeto = None
        self.prioridade = prioridade  # Baixa, Média, Alta
        self.prazo = prazo if prazo else "Sem prazo"

    def atualizar_status(self, novo_status):
        self.status = novo_status


# -----------------------
# Funções de Menu
# -----------------------
def menu():
    print("\n=== SISTEMA DE PROJETOS E TAREFAS ===")
    print("1. Criar Gestor")
    print("2. Criar Projeto")
    print("3. Criar Tarefa")
    print("4. Listar Projetos de um Gestor")
    print("5. Listar Tarefas de um Projeto")
    print("6. Atualizar Status de uma Tarefa")
    print("7. Listar Todas as Tarefas de um Gestor")
    print("0. Sair")


gestores = []  # lista global de gestores


def encontrar_gestor():
    if not gestores:
        print("Nenhum gestor cadastrado ainda.")
        return None
    for i, g in enumerate(gestores, start=1):
        print(f"{i}. {g.nome}")
    escolha = int(input("Escolha o número do gestor: "))
    return gestores[escolha - 1]


def encontrar_projeto(gestor):
    if not gestor.projetos:
        print("Esse gestor não tem projetos cadastrados.")
        return None
    for i, p in enumerate(gestor.projetos, start=1):
        print(f"{i}. {p.nome}")
    escolha = int(input("Escolha o número do projeto: "))
    return gestor.projetos[escolha - 1]


# -----------------------
# Loop principal
# -----------------------
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Gestor: ")
        gestores.append(Gestor(nome))
        print("Gestor criado com sucesso!")

    elif opcao == "2":
        gestor = encontrar_gestor()
        if gestor:
            nome = input("Nome do Projeto: ")
            projeto = Projeto(nome)
            gestor.adicionar_projeto(projeto)
            print("Projeto adicionado ao gestor!")

    elif opcao == "3":
        gestor = encontrar_gestor()
        if gestor:
            projeto = encontrar_projeto(gestor)
            if projeto:
                nome = input("Nome da Tarefa: ")
                descricao = input("Descrição da Tarefa: ")
                prioridade = input("Prioridade (Baixa/Média/Alta): ") or "Média"
                prazo = input("Prazo (dd/mm/aaaa) ou Enter para sem prazo: ")
                tarefa = Tarefa(nome, descricao, prioridade, prazo)
                projeto.adicionar_tarefa(tarefa)
                print("Tarefa criada com sucesso!")

    elif opcao == "4":
        gestor = encontrar_gestor()
        if gestor:
            gestor.listar_projetos()

    elif opcao == "5":
        gestor = encontrar_gestor()
        if gestor:
            projeto = encontrar_projeto(gestor)
            if projeto:
                projeto.listar_tarefas()

    elif opcao == "6":
        gestor = encontrar_gestor()
        if gestor:
            projeto = encontrar_projeto(gestor)
            if projeto:
                projeto.listar_tarefas()
                escolha = int(input("Escolha o número da tarefa: "))
                tarefa = projeto.tarefas[escolha - 1]
                novo_status = input("Novo status (Pendente/Em andamento/Concluída): ")
                tarefa.atualizar_status(novo_status)
                print("Status atualizado com sucesso!")

    elif opcao == "7":
        gestor = encontrar_gestor()
        if gestor:
            gestor.listar_todas_tarefas()

    elif opcao == "0":
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.")
