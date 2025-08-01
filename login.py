# Dados de usuários cadastrados (email: senha)
usuarios = {
    "admin@email.com": "admin123",
    "usuario@email.com": "senha123"
}

print("=== LOGIN ===")
email = input("Email: ")
senha = input("Senha: ")

# Verifica se o email existe e se a senha está correta
if email in usuarios and usuarios[email] == senha:
    print("\nLogin realizado com sucesso!")
else:
    print("\nEmail ou senha incorretos!")
