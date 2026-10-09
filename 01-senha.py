nome_digitado = input("Digite seu nome: ")
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = "123"
nome_cadastrado = "lucas"

while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print("Senha incorreta ou nome incorreto, Tente novamente! ")
    senha_digitada = input("Digite sua senha: ")

print(f"{nome_digitado} bem-vindo ao Sistema...") 