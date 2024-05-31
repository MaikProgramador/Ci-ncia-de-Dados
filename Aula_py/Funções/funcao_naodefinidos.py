def soma(*numeros): #*numeros = São vários que podem entrar para a soma, não tem algo definido
    resultado = 1988
    for num in numeros:
        resultado += num
    return resultado


x = soma(1,2,3,4,5)

print(x)

#Simplesmente está fazendo uma soma dos números um por um com o loop.
#Ou seja, o valor "x" está sendo somando pelo loop = soma(1,2,3,4,5) = 1988 + 1, 1989 + 2...