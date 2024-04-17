"""
13. O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n
fatorial”) e é definido como segue:
n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! =
1 (para n = 0)
Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120.
Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
fatorial.

"""
num = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))

if num < 0:
    print("Número inválido. Digite um número inteiro não negativo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    expressao = f"{num}! = "

    for i in range(num, 0, -1):
        fatorial *= i
        if i == num:
            expressao += str(i)
        else:
            expressao += f" * {i}"

    print(expressao)
    print(f"O fatorial de {num} é {fatorial}.")

