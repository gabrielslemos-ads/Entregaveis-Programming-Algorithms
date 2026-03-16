num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

if operacao == '+': resultado = num1 + num2
elif operacao == '-': resultado = num1 - num2
elif operacao == '*': resultado = num1 * num2
elif operacao == '/': resultado = num1 / num2
else: resultado = None

if resultado is not None:
    print(f"Resultado da operação: {resultado}")
    
    # Análise 1: Par ou Ímpar
    if resultado % 2 == 0: p_i = "par"
    else: p_i = "ímpar"
    
    # Análise 2: Positivo ou Negativo
    if resultado >= 0: p_n = "positivo"
    else: p_n = "negativo"
    
    # Análise 3: Inteiro ou Decimal
    if resultado == round(resultado): i_d = "inteiro"
    else: i_d = "decimal"
    
    print(f"O número é {p_i}, {p_n} e {i_d}.")