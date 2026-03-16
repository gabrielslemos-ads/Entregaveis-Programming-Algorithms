import math

a = float(input("Valor de a: "))
if a == 0:
    print("A equação não é de segundo grau. Encerrando.")
else:
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    
    delta = (b**2) - (4 * a * c)
    
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"Delta zero. Raiz única: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes: {raiz1} e {raiz2}")