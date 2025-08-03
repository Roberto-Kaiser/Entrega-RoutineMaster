usuarios = {
    "Betinho@gmail.com": "betinho123",
    "usuario@gmail.com": "senha123"
}

print("LOGIN:")
email = input("Email: ")
senha = input("Senha: ")

if email in usuarios and usuarios[email] == senha:
    print("\nLogin realizado com sucesso!")
else:
    print("\nEmail ou senha incorretos!")
