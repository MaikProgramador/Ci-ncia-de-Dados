#Utilizar quando a lista for muito grande (milhares)
from array import array

letras = ['a', 'b', 'c', 'd']
numeros = [1,2,3,4,5]
numeros_float = [2.2,3.3,4.4,5.5]

letras_u = array("u", ['a', 'b', 'c', 'd'])
numeros_int = array("i", [1,2,3,4,5])
numeros_f = array("f", [2.2,3.3,4.4,5.5])

print(letras_u)
print(numeros_int)
print(numeros_f)


