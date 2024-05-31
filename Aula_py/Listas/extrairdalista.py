produtos = ["Arroz", "Feijão", "Batata", "Macarrão", 1, 3, 5, 5]

#Salvando todos os produtos nas variaveis conforme os index == 0, 1, 2, 3
#Para evitar problemas na quantidade que quero importar eu aplico isso
#item1, item2, item3, *outros = produtos (Outros é a variável para os outros que n vou usar)
#a variavel "outros" não precisa ficar por último, pode ser no meio ou em outro local
item1, item2, *outros, item3  = produtos

print(item1)
print(item2)
print(item3)
print(outros)