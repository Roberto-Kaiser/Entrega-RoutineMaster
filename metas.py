class GerenciadorMetas:
    def __init__(self):
        self.metas = []
    
    def criar_meta(self):
        print("\n--- Criar Nova Meta ---")
        nome = input("Nome da meta: ")
        data = input("Data da meta (DD/MM/AAAA): ")
        status = "Pendente"  # Status inicial
        
        meta = {
            'nome': nome,
            'data': data,
            'status': status
        }
        
        self.metas.append(meta)
        print(f"\nMeta '{nome}' criada com sucesso!")
    
    def listar_metas(self):
        print("\n--- Suas Metas ---")
        if not self.metas:
            print("Nenhuma meta cadastrada.")
            return
        
        for i, meta in enumerate(self.metas, 1):
            print(f"{i}. {meta['nome']}")
            print(f"   Data: {meta['data']}")
            print(f"   Status: {meta['status']}\n")
    
    def atualizar_status(self):
        self.listar_metas()
        if not self.metas:
            return
        
        try:
            num = int(input("Número da meta para atualizar: ")) - 1
            if 0 <= num < len(self.metas):
                print("\nStatus atuais:")
                print("1. Pendente")
                print("2. Em Progresso")
                print("3. Concluída")
                
                opcao = input("Novo status (1-3): ")
                
                if opcao == "1":
                    self.metas[num]['status'] = "Pendente"
                elif opcao == "2":
                    self.metas[num]['status'] = "Em Progresso"
                elif opcao == "3":
                    self.metas[num]['status'] = "Concluída"
                else:
                    print("Opção inválida.")
                    return
                
                print("Status atualizado com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")
    
    def menu(self):
        while True:
            print("\n=== Gerenciador de Metas ===")
            print("1. Criar nova meta")
            print("2. Ver metas")
            print("3. Atualizar status")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.criar_meta()
            elif opcao == "2":
                self.listar_metas()
            elif opcao == "3":
                self.atualizar_status()
            elif opcao == "4":
                print("Saindo do gerenciador de metas...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciador = GerenciadorMetas()
    gerenciador.menu()
