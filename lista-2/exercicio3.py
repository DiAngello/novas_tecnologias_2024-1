"""
Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem
correta.
Exemplo:
(()) OK
()()(()()) OK
( ) ) Erro
Você pode adicionar elementos à pilha sempre que encontrar abre
parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar,
Listas, Dicionários, Tuplas e Conjuntos 16
verifique se o topo da pilha é um abre parênteses. Se a expressão estiver
correta, sua pilha estará vazia no final.
"""
expressao = input("Digite uma expressão com parênteses: ")

pilha = []  
for char in expressao:
    if char == '(':
        pilha.append(char)  
    elif char == ')':
        if pilha and pilha[-1] == '(':  
            pilha.pop()  
        else:
            pilha.append(char)  
            break  
if len(pilha) == 0:
    print(f"A expressão '{expressao}' está correta.")
else:
    print(f"A expressão '{expressao}' está incorreta.")
