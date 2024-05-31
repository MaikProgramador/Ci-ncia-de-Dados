lista1 = [1, 2, 3, 4]
lista2 = ["a", "b", "c", "d"]

# juntas = lista1 + lista2
# print(juntas)

lista1.extend(lista2)
print(lista1)

#lista dentro de lista
intens = [["item1", "item2"], ["item3", "item4"]]
print(intens[1][0]) #chamando a lista de dentro da lista