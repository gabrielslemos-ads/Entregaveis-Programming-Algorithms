n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media == 10:
    print(f"Aprovado com Distinção! Média: {media:.1f}")
elif media >= 7:
    print(f"Aprovado! Média: {media:.1f}")
else:
    print(f"Reprovado! Média: {media:.1f}")