"""Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45,
78, 36, -17, 2, 12, 8, 3, 3,-52] faça um programa que:
a. imprima o maior elemento;
b. imprima o menor elemento;
c. imprima os números pares;
d. imprima o número de ocorrências do primeiro elemento da lista;
e. imprima a média dos elementos;
f. imprima a soma dos elementos de valor negativo
"""
lista =  [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
print(f'Lista: {lista}')

print("Maior número da lista é:", max(lista))
print("Menor número da lista é:", min(lista))
print("Números pares: ",end=" ")
for num in lista:
    if num % 2 == 0:
        print(f'{num}',end=" ")
print()
print("Número de ocorrências do primeiro elemento: ",lista.count(12))
soma = sum(lista)
media = soma / len(lista)
print(f"Média dos elementos: {media}")
soma_negativos = sum(num for num in lista if num < 0)
print("A soma dos elementos de valor negativo é:", soma_negativos)

