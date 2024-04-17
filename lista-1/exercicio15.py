"""
15. A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros
termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos
dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da
série de Fibonacci.

"""
n = int(input("Digite um número inteiro maior ou igual a 3 para obter o n-ésimo termo da série de Fibonacci: "))

if n < 3:
    print("Número inválido. Digite um número inteiro maior ou igual a 3.")
else:
    termo_antecessor = 1 
    termo_anterior = 1   

    for i in range(3, n + 1):
        termo_atual = termo_antecessor + termo_anterior
        termo_anterior = termo_antecessor
        termo_antecessor = termo_atual

    print(f"O {n}º termo da série de Fibonacci é: {termo_antecessor}")

