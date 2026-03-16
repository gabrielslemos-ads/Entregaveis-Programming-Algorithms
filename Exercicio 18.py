data = input("Digite a data (dd/mm/aaaa): ")

# Divide a string nos lugares onde tem a barra /
dia, mes, ano = data.split("/")
dia, mes, ano = int(dia), int(mes), int(ano)

valida = False

# Meses com 31 dias
if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        valida = True
# Meses com 30 dias
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        valida = True
# Fevereiro (verifica se é bissexto para o dia 29)
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if 1 <= dia <= 29:
            valida = True
    elif 1 <= dia <= 28:
        valida = True

if valida:
    print("Data válida")
else:
    print("Data inválida")