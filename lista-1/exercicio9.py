"""
9. Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção saída seja escolhida.
"""
while True:
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '1':
        operacao = 'adição'
        operador = '+'
    elif escolha == '2':
        operacao = 'subtração'
        operador = '-'
    elif escolha == '3':
        operacao = 'multiplicação'
        operador = '*'
    elif escolha == '4':
        operacao = 'divisão'
        operador = '/'
    elif escolha == '5':
        print("Saindo do programa...")
        break 
    else:
        print("Opção inválida. Escolha uma opção válida (1-5).")
        continue  

    print(f"\nVocê escolheu: {operacao}")

    numero = int(input(f"Digite um número: "))

    print(f"\nTabuada do {numero} ({operacao}):")
    for i in range(1, 11):
        if operador == '/':
            resultado = numero / i
        else:
            resultado = eval(f"{numero} {operador} {i}")
        print(f"{numero} {operador} {i} = {resultado}")
