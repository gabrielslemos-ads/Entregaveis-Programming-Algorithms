# Solicitando o preço dos três produtos
preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

# Verificando qual é o mais barato
if preco1 <= preco2 and preco1 <= preco3:
    print(f"Você deve comprar o primeiro produto, que é o mais barato (R$ {preco1:.2f}).")
elif preco2 <= preco1 and preco2 <= preco3:
    print(f"Você deve comprar o segundo produto, que é o mais barato (R$ {preco2:.2f}).")
else:
    print(f"Você deve comprar o terceiro produto, que é o mais barato (R$ {preco3:.2f}).")