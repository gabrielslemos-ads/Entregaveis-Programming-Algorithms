#Exercício 5 -Faça um programa para a leitura de duas notas parciais de um aluno.

def calcular_media():
    # Lê as duas notas e as converte para números decimais (float)
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Calcula a média
    media = (nota1 + nota2) / 2
    
    # Mostra a média calculada para facilitar a visualização
    print(f"Média alcançada: {media:.1f}")
    
    # Verifica a situação do aluno com base na média
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

# Executa o programa
calcular_media()
