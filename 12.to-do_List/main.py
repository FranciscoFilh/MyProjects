import sqlite3
import os

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela_tarefas(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    ''')
    conn.commit()

# Função para adicionar uma nova tarefa ao banco de dados
def adicionar_tarefa(conn, descricao):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao,))
    conn.commit()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

# Função para listar todas as tarefas do banco de dados
def listar_tarefas(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        print("Lista de Tarefas:")
        for tarefa in tarefas:
            status = " (Concluída)" if tarefa[2] else " (Pendente)"
            print(f"{tarefa[0]}. {tarefa[1]}{status}")

# Função para marcar uma tarefa como concluída no banco de dados
def marcar_como_concluida(conn, id_tarefa):
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id_tarefa,))
    conn.commit()
    print(f"Tarefa marcada como concluída.")

# Função para remover uma tarefa do banco de dados
def remover_tarefa(conn, id_tarefa):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
    conn.commit()
    print(f"Tarefa removida com sucesso.")

# Função principal que controla o fluxo do programa
def main():
    # Obtém o diretório atual do arquivo Python
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'tarefas.db')

    conn = sqlite3.connect(caminho_bd)
    criar_tabela_tarefas(conn)

    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("Escolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(conn, descricao)
        elif opcao == '2':
            listar_tarefas(conn)
        elif opcao == '3':
            id_tarefa = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            marcar_como_concluida(conn, id_tarefa)
        elif opcao == '4':
            id_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
            remover_tarefa(conn, id_tarefa)
        elif opcao == '5':
            print("Saindo do Gerenciador de Tarefas...")
            break
        else:
            print("Opção inválida! Por favor, digite um número de 1 a 5.")

    conn.close()

if __name__ == "__main__":
    main()
