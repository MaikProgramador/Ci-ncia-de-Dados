def agencia(**carro): #os "**" significam que eu posso ter vários argumentos e vários parametros
    return carro

x = print(agencia(modelo="Jetta", cor="Cinza", motor=2.0, placa=9))
y = print(agencia(modelo="Jetta", cor="Preto", motor=2.0, placa=19999))
z = print(agencia(modelo="Jetta", cor="Branca", motor=2.0, placa=12332))

print(x)
print(y)
print(z)