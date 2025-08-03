class GerenciadorGrupos:
    def __init__(self):
        self.grupos = []
    
    def criar_grupo(self):
        print("\n--- Criar Novo Grupo ---")
        nome = input("Nome do grupo: ")
        atividades = input("Atividades propostas (separadas por vírgula): ").split(',')
        comentarios = []
        
        grupo = {
            'nome': nome,
            'atividades': [atividade.strip() for atividade in atividades],
            'comentarios': comentarios
        }
        
        self.grupos.append(grupo)
        print(f"\nGrupo '{nome}' criado com sucesso!")
    
    def adicionar_comentario(self):
        self.listar_grupos()
        if not self.grupos:
            return
        
        try:
            num = int(input("Número do grupo para comentar: ")) - 1
            if 0 <= num < len(self.grupos):
                comentario = input("Digite seu comentário: ")
                self.grupos[num]['comentarios'].append(comentario)
                print("Comentário adicionado!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")
    
    def listar_grupos(self):
        print("\n--- Grupos Disponíveis ---")
        if not self.grupos:
            print("Nenhum grupo cadastrado.")
            return
        
        for i, grupo in enumerate(self.grupos, 1):
            print(f"\n{i}. {grupo['nome']}")
            print("   Atividades:", ", ".join(grupo['atividades']))
            print("   Comentários:")
            for comentario in grupo['comentarios']:
                print(f"   - {comentario}")
    
    def menu(self):
        while True:
            print("\n=== Gerenciador de Grupos ===")
            print("1. Criar novo grupo")
            print("2. Listar grupos")
            print("3. Adicionar comentário")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.criar_grupo()
            elif opcao == "2":
                self.listar_grupos()
            elif opcao == "3":
                self.adicionar_comentario()
            elif opcao == "4":
                print("Saindo do gerenciador de grupos...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciador = GerenciadorGrupos()
    gerenciador.menu()
