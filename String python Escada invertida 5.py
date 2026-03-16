# 5. Escada invertida: Mostre o nome em escada decrescente. [cite: 7]

nome = input("Digite seu nome: ")
for i in range(len(nome), 0, -1):
    print(nome[:i])