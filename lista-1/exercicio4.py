"""
4. Escreva um aplicativo que insere um número consistindo em cinco dígitos
do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.

"""
num = input("Digite um número de cinco dígitos: ")

if len(num) != 5:
        print("Por favor, insira um número válido de cinco dígitos.")
else:    
    num = list(num)
    print("   ".join(num))
