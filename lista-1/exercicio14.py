"""
14. O quadrado de um número natural n é dado pela soma dos n primeiros
números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado
um número n, calcule seu quadrado usando a soma de ímpares ao invés de
produto.

"""
num = int(input("Digite um número: "))

aux = num
soma = 0

while aux > 0:
    soma = soma + 1 + (aux-1)*2
    aux -=1

print(f"O quadrado de {num} é {soma}")
