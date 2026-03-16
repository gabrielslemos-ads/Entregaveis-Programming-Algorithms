# 8. Palindromo: Leia uma sequência de caracteres e informe se é um palíndromo. [cite: 10]

frase = input("Digite uma frase ou palavra: ").replace(" ", "").lower()

if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")