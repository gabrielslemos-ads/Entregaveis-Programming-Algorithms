# 4. Nome em escada: Mostre o nome em formato de escada crescente. [cite: 6]

nome = input("Digite seu nome: ")
for i in range(1, len(nome) + 1):
    print(nome[:i])