"""
1. Escreva um programa que gere um dicionário, em que cada chave seja um
caractere, e seu valor seja o número desse caractere encontrado em uma
frase lida.
Exemplo:O rato ->
{"O":1,"r":1,"a":1,"t":1,"o":1}
"""
d={}
for letra in "Castelo de cartas":
    if letra in d:
        d[letra] = d[letra] +1
    else:
        d[letra] =1
print(d)
