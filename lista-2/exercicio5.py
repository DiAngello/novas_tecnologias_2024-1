"""
Escreva um programa que copie os valores pares para uma lista e os
valores ímpares para outra lista. A lista inicialmente de valores é V=
[9,8,7,12,0,13,21] .
"""
lista = [9, 8, 7, 12, 0, 13, 21]
lista_par = []
lista_impar = []

print(f'Lista: {lista}')

for num in lista:
    if num % 2 == 0:
        lista_par.append(num)  
    else:
        lista_impar.append(num)  

print("Valores pares:", lista_par)
print("Valores ímpares:", lista_impar)
