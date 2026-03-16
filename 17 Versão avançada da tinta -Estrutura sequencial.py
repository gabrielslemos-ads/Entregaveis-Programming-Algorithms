import math

area_a_pintar = float(input("Digite a área em m²: "))

# Adicionando 10% de folga (multiplicar por 1.1) e calculando litros
# cobertura é de 6 metros por litro
litros_com_folga = (area_a_pintar / 6) * 1.1

# Opção 1: Comprar apenas latas de 18L
latas_apenas = math.ceil(litros_com_folga / 18)
preco_latas = latas_apenas * 80

# Opção 2: Comprar apenas galões de 3,6L
galoes_apenas = math.ceil(litros_com_folga / 3.6)
preco_galoes = galoes_apenas * 25

# Opção 3: Misturar latas e galões (Melhor custo-benefício)
latas_mistas = int(litros_com_folga // 18)
litros_restantes = litros_com_folga % 18
galoes_mistos = math.ceil(litros_restantes / 3.6)
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

print(f"Apenas latas: {latas_apenas} unidades | R$ {preco_latas:.2f}")
print(f"Apenas galões: {galoes_apenas} unidades | R$ {preco_galoes:.2f}")
print(f"Mistura (melhor): {latas_mistas} latas e {galoes_mistos} galões | R$ {preco_misto:.2f}")