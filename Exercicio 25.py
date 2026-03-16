print("Responda 1 para SIM ou 0 para NÃO:")
p1 = int(input("Telefonou para a vítima? "))
p2 = int(input("Esteve no local do crime? "))
p3 = int(input("Mora perto da vítima? "))
p4 = int(input("Devia para a vítima? "))
p5 = int(input("Já trabalhou com a vítima? "))

soma_respostas = p1 + p2 + p3 + p4 + p5

if soma_respostas == 2:
    print("Classificação: Suspeita")
elif 3 <= soma_respostas <= 4:
    print("Classificação: Cúmplice")
elif soma_respostas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")