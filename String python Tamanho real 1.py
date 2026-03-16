# 1. Tamanho de strings: Leia duas strings, mostre o conteúdo e o tamanho de cada uma. [cite: 2]
# Informe se possuem o mesmo tamanho e se o conteúdo é igual ou diferente. [cite: 3]

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")

print(f"String 1: {s1} | Tamanho: {len(s1)} caracteres")
print(f"String 2: {s2} | Taman length: {len(s2)} caracteres")

if len(s1) == len(s2):
    print("As duas strings são do mesmo tamanho.")
else:
    print("As duas strings são de tamanhos diferentes.")

if s1 == s2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdo diferente.")