compra_realizada = False
dados_da_compra = "Compra realizada no valor de R$12.50"

for enviar in range(3):
    if compra_realizada:
        print(dados_da_compra)
        print("Mais informações no seu email")
        break
else:
    print("Falha na compra")