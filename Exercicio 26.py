litros = float(input("Quantos litros foram vendidos? "))
combustivel = input("Tipo de combustível (A-álcool, G-gasolina): ").upper()

preco_gasolina = 2.50
preco_alcool = 1.90

if combustivel == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    total = litros * (preco_alcool * (1 - desconto))
elif combustivel == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    total = litros * (preco_gasolina * (1 - desconto))

print(f"O valor total a ser pago é R$ {total:.2f}")