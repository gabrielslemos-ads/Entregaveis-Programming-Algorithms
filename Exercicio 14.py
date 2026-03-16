n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2

if media >= 9: conceito = "A"
elif media >= 7.5: conceito = "B"
elif media >= 6: conceito = "C"
elif media >= 4: conceito = "D"
else: conceito = "E"

situacao = "APROVADO" if conceito in "ABC" else "REPROVADO"

print(f"Notas: {n1}, {n2} | Média: {media} | Conceito: {conceito} | Status: {situacao}")