#Transformando tudo em lista:
var = list("comprar")
print(var)

#juntando essas listas com index juntos. Exp: (0:0) (1:1)...
nome = ["maik", "carlos", "leo"]
idade = ["24", "26", "22"]

duas_listas = zip(nome, idade)
print(list(duas_listas))