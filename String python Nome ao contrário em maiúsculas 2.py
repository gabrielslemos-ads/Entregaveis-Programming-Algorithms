# 2. Nome ao contrário em maiúsculas: Leia o nome do usuário e mostre-o de trás para frente em letras maiúsculas. [cite: 4]

nome = input("Digite seu nome: ")
# O fatiamento [::-1] inverte a string
print(f"Nome invertido: {nome[::-1].upper()}")