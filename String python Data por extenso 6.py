# 6. Data por extenso: Leia uma data (dd/mm/aaaa) e mostre no formato '29 de Outubro de 1973'. [cite: 8]

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

data = input("Informe a data (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')

# Convertemos o mês para int e subtraímos 1 pois a lista começa no índice 0
mes_extenso = meses[int(mes) - 1]

print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")