# Pede os três números para o usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica se o num1 é o maior de todos
if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)

# Se o num1 não for o maior, verifica se o num2 é o maior
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)

# Se nem o num1 e nem o num2 forem os maiores, só sobra o num3
else:
    print("O maior número é:", num3)