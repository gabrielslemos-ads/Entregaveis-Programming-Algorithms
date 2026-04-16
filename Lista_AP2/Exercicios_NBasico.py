# 1. Olá Nome:
# Crie uma função chamada saudacao(nome) que receba um nome como
# argumento e imprima "Olá, [nome]!".
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Gabriel")
git config --global user.email "seu_email_do_github@exemplo.com"
# 2. Área do Retângulo:
# Escreva uma função calcular_area(base, altura) que retorne a área.
def calcular_area(base, altura):
    return base * altura

# 3. Maior de Dois:
# Faça uma função maior_valor(a, b) que receba dois números e retorne o maior.
def maior_valor(a, b):
    if a > b:
        return a
    else:
        return b

# 4. Par ou Ímpar:
# Crie uma função verificar_par(numero) que retorne True se for par e False caso contrário.
def verificar_par(numero):
    return numero % 2 == 0

# 5. Média Simples:
# Escreva uma função que receba três notas e retorne a média aritmética simples.
def calcular_media_simples(n1, n2, n3):
    return (n1 + n2 + n3) / 3