"""
2. Escreva um programa que compare duas listas. Utilizando operações com
conjuntos, imprima:
a. os valores comuns às duas listas
b. os valores que só existem na primeira
c. os valores que existem apenas na segunda
d. uma lista com os elementos não repetidos das duas listas.
e. a primeira lista sem os elementos repetidos na segunda.
"""
a = {'Slipknot', 'Bauhaus', 'Gojira', 'Slayer'}
b = {'The Cure', 'Deftones', 'Gojira', 'Exodus'}

interseçao = a&b
print(interseçao)

diferenca1 = a-b
print(diferenca1)

diferenca2 = b-a
print(diferenca2)

nRepetidos = diferenca1|diferenca2
print(nRepetidos)

diferenca1 = a-b
print(diferenca1)
