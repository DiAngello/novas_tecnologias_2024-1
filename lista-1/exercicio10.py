"""
10. Escreva um programa que leia um número e verifique se é ou não um
número primo.
"""
num = int(input("Digite um número: "))

if num == 1:
    print(f"O número {num} não é primo.")
else:
    eh_primo = True  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
