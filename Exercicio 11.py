salario_atual = float(input("Digite o salário atual: "))

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

print(f"Salário antes: R$ {salario_atual:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")