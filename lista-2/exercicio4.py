"""
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T= [
-10, -8, 0, 1, 2, 5, -2,-4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.
"""
lista = [-10, -8, 0, 1, 2, 5, -2,-4]
print(f'Lista de temperaturas: {lista}')

print("Maior temperatura:", max(lista))
print("Menor temperatura:", min(lista))
soma = sum(lista)
media = soma / len(lista)
print(f"Média das temperaturas: {media}")
