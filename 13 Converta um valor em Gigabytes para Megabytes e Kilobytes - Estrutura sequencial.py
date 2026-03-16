gb = float(input("Digite o valor em Gigabytes (GB): "))

mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB equivalem a {mb:.0f} MB e {kb:.0f} KB")