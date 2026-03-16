# 13. Palavra embaralhada: Mostre uma palavra com letras embaralhadas e permita que o usuário adivinhe. [cite: 15]

import random

palavras = ["gabriel", "computador", "passarinho", "malasya"]
original = random.choice(palavras)

# Transforma a string em lista, embaralha e junta de novo
embaralhada = list(original)
random.shuffle(embaralhada)
embaralhada = "".join(embaralhada)

print(f"Adivinhe a palavra: {embaralhada}")
chute = input("Seu palpite: ").lower()

if chute == original:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena! A palavra era: {original}")