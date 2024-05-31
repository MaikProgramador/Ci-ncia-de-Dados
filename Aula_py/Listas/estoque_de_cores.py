usuario = input("Escolha a sua cor: ")
cores = ["amarelo", "vermelho", "verde", "azul"]


if usuario.lower() in cores: #Colocando tudo em minúsculo
    print(f"A cor {cores[0]} está em estoque")
else:
    print(f"A cor{cores[0]} não está em estoque")

