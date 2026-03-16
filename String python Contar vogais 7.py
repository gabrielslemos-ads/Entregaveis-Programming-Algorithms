# 7. Contar espaços e vogais: Dada uma frase, conte quantos espaços existem e quantas vezes aparecem as vogais. [cite: 9]

frase = input("Digite uma frase: ").lower()
espacos = frase.count(" ")
vogais = 0

for letra in frase:
    if letra in "aeiou":
        vogais += 1

print(f"A frase contém {espacos} espaços e {vogais} vogais.")