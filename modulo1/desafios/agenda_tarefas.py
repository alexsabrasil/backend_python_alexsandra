# Passo 1: Criar uma lista vazia para armazenar as tarefas
tarefas = []

# Passo 2: Usar um loop while para cadastrar tarefas
while True:
    # Pedir a tarefa ao usuário
    tarefa = input("Digite uma tarefa (ou 'sair' para finalizar): ")
    
    # Verificar se o usuário quer parar
    if tarefa.lower() == 'sair':
        break  # Sai do loop
    
    # Adicionar a tarefa à lista
    tarefas.append(tarefa)

# Passo 3: Exibir todas as tarefas cadastradas
print("\nSua agenda de tarefas:")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}. {tarefa}")