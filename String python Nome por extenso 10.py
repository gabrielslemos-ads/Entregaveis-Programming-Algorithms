# 10. Número por extenso: Leia um número até 99 e mostre-o por extenso. [cite: 12]

unidades = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", 
            "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

num = int(input("Digite um número de 0 a 99: "))

if 0 <= num < 20:
    print(unidades[num])
elif 20 <= num < 100:
    d = num // 10
    u = num % 10
    if u == 0:
        print(dezenas[d])
    else:
        print(f"{dezenas[d]} e {unidades[u].lower()}")
else:
    print("Número fora do intervalo solicitado.")