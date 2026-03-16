tamanho_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velocidade da internet (Mbps): "))

# Velocidade em Mbps precisa ser dividida por 8 para virar MB/s
tempo_segundos = tamanho_mb / (velocidade_mbps / 8)
tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")