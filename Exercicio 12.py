valor_hora = float(input("Valor da hora: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

ir_valor = salario_bruto * (ir_percentual / 100)
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
total_descontos = ir_valor + inss
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%): R$ {ir_valor:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")