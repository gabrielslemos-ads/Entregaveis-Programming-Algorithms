peso = float(input("Digite o peso de peixes (kg): "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")