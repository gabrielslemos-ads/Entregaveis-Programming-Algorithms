# Pede para o usuário digitar a letra do turno
print("Em que turno você estuda?")
print("Digite M para Matutino, V para Vespertino ou N para Noturno:")
turno = input()

# Verifica se digitou M (maiúsculo) OU m (minúsculo)
if turno == "M" or turno == "m":
    print("Bom Dia!")

# Verifica se digitou V (maiúsculo) OU v (minúsculo)
elif turno == "V" or turno == "v":
    print("Boa Tarde!")

# Verifica se digitou N (maiúsculo) OU n (minúsculo)
elif turno == "N" or turno == "n":
    print("Boa Noite!")

# Se o usuário digitar qualquer outra coisa (tipo X, 1, 2, etc)
else:
    print("Valor Inválido!")