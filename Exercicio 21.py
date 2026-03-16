valor = int(input("Qual valor deseja sacar? (R$ 10 a R$ 600): "))

if 10 <= valor <= 600:
    # Calculado as notas da maior para a menor
    notas100 = valor // 100
    valor %= 100
    
    notas50 = valor // 50
    valor %= 50
    
    notas10 = valor // 10
    valor %= 10
    
    notas5 = valor // 5
    valor %= 5
    
    notas1 = valor
    
    print(f"Notas fornecidas: ")
    print(f"100 reais: {notas100}")
    print(f"50 reais: {notas50}")
    print(f"10 reais: {notas10}")
    print(f"5 reais: {notas5}")
    print(f"1 real: {notas1}")
else:
    print("Valor inválido para saque.")