"""
12. Modifique o programa anterior de forma a ler um número n. Imprima os n
primeiros números primos.

"""
n = int(input("Digite a quantidade de números primos que deseja encontrar: "))

primos_encontrados = 0
num = 2

primos = []

while primos_encontrados < n:
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        primos.append(num)
        primos_encontrados += 1  

    num += 1

print(f"Os primeiros {n} números primos são: {primos}")
