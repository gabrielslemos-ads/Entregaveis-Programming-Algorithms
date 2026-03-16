# Pede os três números para o usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print("Os números em ordem decrescente são:")

# Combinação 1: num1 é o maior, num2 é o do meio, num3 é o menor
if num1 >= num2 and num2 >= num3:
    print(num1, "-", num2, "-", num3)

# Combinação 2: num1 é o maior, num3 é o do meio, num2 é o menor
elif num1 >= num3 and num3 >= num2:
    print(num1, "-", num3, "-", num2)

# Combinação 3: num2 é o maior, num1 é o do meio, num3 é o menor
elif num2 >= num1 and num1 >= num3:
    print(num2, "-", num1, "-", num3)

# Combinação 4: num2 é o maior, num3 é o do meio, num1 é o menor
elif num2 >= num3 and num3 >= num1:
    print(num2, "-", num3, "-", num1)

# Combinação 5: num3 é o maior, num1 é o do meio, num2 é o menor
elif num3 >= num1 and num1 >= num2:
    print(num3, "-", num1, "-", num2)

# Combinação 6: Se não for nenhuma das anteriores, só sobra esta opção
else:
    print(num3, "-", num2, "-", num1)