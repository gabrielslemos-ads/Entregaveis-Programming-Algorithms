# 11. Jogo da Forca: Desenvolva um jogo simples da forca usando uma lista de palavras. [cite: 13]

import random

palavras = ["GABRIEL", "SISTEMAS", "IMPACTA", "ARVORE", "ALUNO"]
palavra_secreta = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra_secreta]
erros = 0
max_erros = 6

print("--- JOGO DA FORCA ---")

while "_" in letras_descobertas and erros < max_erros:
    print(f"\nPalavra: {' '.join(letras_descobertas)}")
    print(f"Erros: {erros}/{max_erros}")
    palpite = input("Digite uma letra: ").upper()

    if palpite in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_descobertas[i] = palpite
    else:
        erros += 1
        print("Errou!")

if "_" not in letras_descobertas:
    print(f"\nParabéns! Você ganhou. A palavra era: {palavra_secreta}")
else:
    print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")