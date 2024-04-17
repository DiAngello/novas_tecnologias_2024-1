"""
Numa certa agência bancária, as contas são identificadas por números de
até seis dígitos seguidos de um dígito verificador, calculado conforme
exemplificado a seguir. Dado um número de conta n, exiba o número de
conta completo correspondente. Seja n = 7314 o número da conta.
Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15;
Calculamos o resto da divisão de s por 10 e obtemos o dígito d = 5. Número
de conta completo: 007314−5
"""
n = input("Digite o número da conta: ")

soma_digitos = sum(int(digito) for digito in n)

digito_verificador = soma_digitos % 10

numero_completo = f"{n:0>6}-{digito_verificador}"

print(f"Número de conta completo: {numero_completo}")
