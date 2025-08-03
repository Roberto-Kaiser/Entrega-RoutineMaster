class Feedback:
    def __init__(self):
        self.nota = 0
        self.descricao = "Sem feedback"

    def enviar_feedback(self):
        while True:
            try:
                nova_nota = int(input("Digite a nota (0-10): "))
                if 0 <= nova_nota <= 10:
                    self.nota = nova_nota
                    break
                else:
                    print("Nota deve ser entre 0 e 10")
            except ValueError:
                print("Digite um número válido")

        self.descricao = input("Digite sua descrição: ") or self.descricao
        print("Feedback enviado!")

    def mostrar_feedback(self):
        print(f"\nNota: {self.nota}/10")
        print(f"Descrição: {self.descricao}")

    def menu(self):
        while True:
            print("\n1. Enviar feedback")
            print("2. Ver feedback")
            print("3. Sair")
            opcao = input("Escolha: ")

            if opcao == "1":
                self.enviar_feedback()
            elif opcao == "2":
                self.mostrar_feedback()
            elif opcao == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    sistema_feedback = Feedback()
    sistema_feedback.menu()
