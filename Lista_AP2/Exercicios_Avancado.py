# ==========================================
# 1. Validação de Entrada (leiaInt)
# ==========================================
def leiaInt(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("ERRO! Digite um número inteiro válido.")

# --- TESTE DO EX 1 ---
print("Teste Ex 1:")
n = leiaInt("Digite um número: ")
print(f"Sucesso! O número {n} foi aceito.\n")


# ==========================================
# 2. Função com Argumentos Opcionais
# ==========================================
def configurar_perfil(nome, idade, cidade="Desconhecida"):
    print(f"-> Perfil: {nome}, {idade} anos, Cidade: {cidade}")

# --- TESTE DO EX 2 ---
print("Teste Ex 2:")
configurar_perfil("Gabriel", 20, "São Paulo")
configurar_perfil("Lemos", 25) # Teste sem a cidade
print()


# ==========================================
# 3. Recursão (Fibonacci)
# ==========================================
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# --- TESTE DO EX 3 ---
print("Teste Ex 3 (Fibonacci):")
termos = 5 
print(f"Primeiros {termos} números: ", end="")
for i in range(termos):
    print(fibonacci(i), end=" ")
print("\n")


# ==========================================
# 4. Escopo de Variáveis
# ==========================================
variavel_global = "GLOBAL"

def demonstrar_escopo():
    variavel_local = "LOCAL"
    print(f"-> Consigo ver a: {variavel_global}")
    print(f"-> Consigo ver a: {variavel_local}")

# --- TESTE DO EX 4 ---
print("Teste Ex 4 (Escopo):")
demonstrar_escopo()
print()


# ==========================================
# 5. Processamento de Lista com Dicionário
# ==========================================
def produto_mais_caro(lista_produtos):
    mais_caro = lista_produtos[0]
    for produto in lista_produtos:
        if produto['preco'] > mais_caro['preco']:
            mais_caro = produto
    return mais_caro

# --- TESTE DO EX 5 ---
print("Teste Ex 5 (Produtos):")
mercado = [
    {"nome": "Arroz", "preco": 25.50},
    {"nome": "Carne", "preco": 45.00}
]
caro = produto_mais_caro(mercado)
print(f"O item mais caro é: {caro['nome']} (R$ {caro['preco']})")


