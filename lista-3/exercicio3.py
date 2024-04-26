"""
9. Escreva um programa que compare duas listas. Considere a primeira lista
como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conjuntos, seu programa deverá imprimir a lista
de modificações entre essas duas versões, listando:
 ◦ os elementos que não mudaram
 ◦ os novos elementos
 ◦ os elementos que foram removidos
 """
a = {'banana','laranja','melancia', 'morango'}
b = {'morango','laranja','mamão','maçã'}

for frutas in a:
    if frutas in b:
        print({frutas}, end = ' ')
        
print()

for frutas in b:
    if frutas not in a:
        print({frutas}, end = ' ')

print()

for frutas in a:
    if frutas not in b:
         print({frutas}, end = ' ')
