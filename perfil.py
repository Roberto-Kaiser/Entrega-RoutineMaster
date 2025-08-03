class Perfil:
    def __init__(self):
        self.nome = "Sem nome"
        self.idade = 0
        self.genero = "Não especificado"
        self.descricao = "Sem descrição"
    
    def editar_perfil(self):
        print("\n--- Editar Perfil ---")
        self.nome = input(f"Nome atual: {self.nome}\nNovo nome: ") or self.nome
        self.idade = int(input(f"Idade atual: {self.idade}\nNova idade: ") or self.idade)
        self.genero = input(f"Gênero atual: {self.genero}\nNovo gênero: ") or self.genero
        self.descricao = input(f"Descrição atual: {self.descricao}\nNova descrição: ") or self.descricao
        print("Perfil atualizado com sucesso!")
    
    def mostrar_perfil(self):
        print("\n--- Meu Perfil ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Gênero: {self.genero}")
        print(f"Descrição: {self.descricao}")
    
    def menu(self):
        while True:
            print("\n--- Menu do Perfil ---")
            print("1. Ver perfil")
            print("2. Editar perfil")
            print("3. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.mostrar_perfil()
            elif opcao == "2":
                self.editar_perfil()
            elif opcao == "3":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    meu_perfil = Perfil()
    meu_perfil.menu()
