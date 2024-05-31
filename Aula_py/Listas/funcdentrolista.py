#listas servem para armezenar mais dados em uma variável
#Manter sequência dos dados em uma variável

cidades = ["São Paulo", "Rio de Janeiro", "Salvador"]

#Trocando valor da variável em lista
cidades[0] = "Curitiba"

#funções dentro da lista.
# cidades.sort() #Vai deixar a lista em ordem alfabetica
# cidades.pop(0) #Arrancar de dentro da lista o index referido
cidades.remove("Curitiba")
cidades.insert(1, "Baianos") #Inserir uma informação a lista no index desejado
cidades.append("Los Santos") #Adiciona um valor à lista

print(cidades[0])
print(cidades)