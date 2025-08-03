class GerenciadorEventos:
    def __init__(self):
        self.eventos = []
    
    def criar_evento(self):
        print("\n--- Criar Novo Evento ---")
        nome = input("Nome do evento: ")
        
        grupos = []
        while True:
            grupo = input("Adicione um grupo participante (ou deixe em branco para terminar): ")
            if not grupo:
                break
            grupos.append(grupo)
        
        atividades = []
        while True:
            atividade = input("Adicione uma atividade ao evento (ou deixe em branco para terminar): ")
            if not atividade:
                break
            atividades.append(atividade)
        
        descricao = input("Descrição do evento: ")
        
        evento = {
            'nome': nome,
            'grupos': grupos,
            'atividades': atividades,
            'descricao': descricao,
            'votos': 0
        }
        
        self.eventos.append(evento)
        print(f"\nEvento '{nome}' criado com sucesso!")
    
    def listar_eventos(self):
        print("\n--- Eventos Disponíveis ---")
        if not self.eventos:
            print("Nenhum evento cadastrado.")
            return
        
        for i, evento in enumerate(self.eventos, 1):
            print(f"\n{i}. {evento['nome']}")
            print(f"   Descrição: {evento['descricao']}")
            print("   Grupos participantes:", ", ".join(evento['grupos']))
            print("   Atividades:", ", ".join(evento['atividades']))
            print(f"   Votos: {evento['votos']}")
    
    def votar_evento(self):
        self.listar_eventos()
        if not self.eventos:
            return
        
        try:
            num = int(input("Número do evento para votar: ")) - 1
            if 0 <= num < len(self.eventos):
                self.eventos[num]['votos'] += 1
                print(f"Voto registrado para '{self.eventos[num]['nome']}'!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")
    
    def menu(self):
        while True:
            print("\n=== Gerenciador de Eventos ===")
            print("1. Criar novo evento")
            print("2. Listar eventos")
            print("3. Votar em evento")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.criar_evento()
            elif opcao == "2":
                self.listar_eventos()
            elif opcao == "3":
                self.votar_evento()
            elif opcao == "4":
                print("Saindo do gerenciador de eventos...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciador = GerenciadorEventos()
    gerenciador.menu()
