"""
1. Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do
usuário esses números e imprime sua soma, produto, diferença e divisão.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


soma = num1 + num2
diferenca = num1 - num2
divisao = num1 / num2
produto = num1 * num2

print(f"A soma dos números {num1} e {num2} é: {soma}")
print(f"A diferença dos números {num1} e {num2} é: {diferenca}")
print(f"A divisão dos números {num1} e {num2} é: {divisao}")
print(f"O produto dos números {num1} e {num2} é: {produto}")
