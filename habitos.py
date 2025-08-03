class GerenciadorHabitos:
    def __init__(self):
        self.habitos = []

    def adicionar_habito(self):
        print("\n--- Adicionar Novo Hábito ---")
        nome = input("Nome do hábito: ")
        horario = input("Horário (ex: 08:30): ")
        frequencia = input("Frequência (ex: Diária, Semanal): ")
        
        habito = {
            'nome': nome,
            'horario': horario,
            'frequencia': frequencia
        }
        
        self.habitos.append(habito)
        print(f"\nHábito '{nome}' adicionado com sucesso!")

    def listar_habitos(self):
        print("\n--- Seus Hábitos ---")
        if not self.habitos:
            print("Nenhum hábito cadastrado.")
            return
        
        for i, habito in enumerate(self.habitos, 1):
            print(f"{i}. {habito['nome']}")
            print(f"   Horário: {habito['horario']}")
            print(f"   Frequência: {habito['frequencia']}\n")

    def menu(self):
        while True:
            print("\n=== Gerenciador de Hábitos ===")
            print("1. Adicionar hábito")
            print("2. Listar hábitos")
            print("3. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_habito()
            elif opcao == "2":
                self.listar_habitos()
            elif opcao == "3":
                print("Saindo do gerenciador de hábitos...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciador = GerenciadorHabitos()
    gerenciador.menu()
