# 1. Calculadora de Média de Lista
def calcular_media_lista(notas):
    total_soma = sum(notas)    
    quantidade = len(notas)     
    return total_soma / quantidade

notas_sala = [10, 9, 8, 7]
print(f"1. Média da lista {notas_sala}: {calcular_media_lista(notas_sala)}")

# 2. Conversor de Temperatura
def celsius_para_fahrenheit(celsius):
 
    resultado_f = (celsius * 9/5) + 32
    return resultado_f
temp = float(input("2. Digite Celsius para converter: "))
print(f"Fahrenheit: {celsius_para_fahrenheit(temp)}°F")

# 3. Contador de Vogais
def contar_vogais(frase):
    lista_vogais = "aeiouAEIOU"
    seguranca_contador = 0
    
    for letra in frase:
        if letra in lista_vogais:
            seguranca_contador += 1 # Se for vogal, conta +1
            
    return seguranca_contador

texto_usuario = input("3. Digite uma frase para contar vogais: ")
print(f"Vogais encontradas: {contar_vogais(texto_usuario)}")


# 4. Fatorial (Contagem Regressiva)
def calcular_fatorial(numero):
    resultado_final = 1
    # Cria uma fila de números para multiplicar
    for atual in range(1, numero + 1):
        resultado_final *= atual
    return resultado_final

num_fatorial = int(input("4. Digite um número para o Fatorial: "))
print(f"O fatorial de {num_fatorial} é {calcular_fatorial(num_fatorial)}")


# 5. Inverter String (O Espelho)
def inverter_texto(texto_original):
    # O truque [::-1] lê a frase de trás para frente
    return texto_original[::-1]

frase_normal = input("5. Digite algo para inverter: ")
print(f"Invertido: {inverter_texto(frase_normal)}")