import math

area_a_pintar = float(input("Digite o tamanho da área em metros quadrados: "))

# 1 litro para cada 3 metros
litros_necessarios = area_a_pintar / 3

# Cada lata tem 18 litros. math.ceil arredonda para cima para não faltar tinta.
quantidade_latas = math.ceil(litros_necessarios / 18)
preco_total = quantidade_latas * 80

print(f"Você precisará de {quantidade_latas} latas.")
print(f"Preço total: R$ {preco_total:.2f}")