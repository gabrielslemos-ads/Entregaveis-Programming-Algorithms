

def verificar_letra():
    # Pede ao usuário para digitar uma letra e converte para minúscula
    letra = input("Digite uma letra: ").lower()

    # Verifica se o usuário digitou exatamente um caractere e se é uma letra do alfabeto
    if len(letra) == 1 and letra.isalpha():
        # Verifica se a letra está no grupo das vogais
        if letra in 'aeiou':
            print(f"A letra '{letra}' é uma vogal.")
        else:
            print(f"A letra '{letra}' é uma consoante.")
    else:
        print("Entrada inválida! Por favor, digite apenas uma única letra do alfabeto.")

# Executa a função
verificar_letra()