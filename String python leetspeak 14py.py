# 14. Leet Speak: Leia um texto e converta para a escrita estilo leet (ex: 1337). [cite: 16]

tabela = {
    'a': '4', 'e': '3', 'i': '1', 'o': '0', 't': '7', 's': '5', 'b': '8'
}

texto = input("Digite o texto para converter: ").lower()
resultado = ""

for caractere in texto:
    # Se o caractere estiver na tabela, troca. Se não, mantém o original.
    resultado += tabela.get(caractere, caractere)

print(f"Texto convertido: {resultado}")
