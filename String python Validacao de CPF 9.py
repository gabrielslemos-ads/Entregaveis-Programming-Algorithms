# 9. Verificação de CPF: Leia um CPF no formato xxx.xxx.xxx-xx e valide os dígitos verificadores. [cite: 11]

cpf_input = input("Digite o CPF (xxx.xxx.xxx-xx): ")
# Remove pontos e traço
cpf = cpf_input.replace(".", "").replace("-", "")

if len(cpf) == 11 and cpf.isdigit():
    print(f"O CPF {cpf_input} possui formato válido.")
    # Nota: Para uma validação real de dígitos verificadores, 
    # seriam necessários cálculos matemáticos específicos do algoritmo do CPF.
else:
    print("CPF inválido (formato incorreto).")