# 12. Corrigir telefone: Leia um telefone com 7 ou 8 dígitos e ajuste adicionando o '3' se necessário. [cite: 14]

telefone = input("Telefone: ").replace("-", "")

if len(telefone) == 8:
    print("Telefone possui 8 dígitos. Vou adicionar o 3 na frente.")
    telefone = "3" + telefone

print(f"Telefone corrigido: {telefone[:4]}-{telefone[4:]}")
