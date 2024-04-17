"""
11. Coloque um número bem grande para ser executado no exemplo anterior,
você perceberá que demora bastante, consegue pensar num solução na
lógica para reduzir o tempo de procura?
"""
num = int(input("Digite um número: "))

if num <= 1:
    print(f"O número {num} não é primo.")
else:
    if num == 2:
        print(f"O número {num} é primo.")
    elif num % 2 == 0:
        print(f"O número {num} não é primo.")
    else:
        eh_primo = True 

        limite = num // 2 + 1
        for i in range(3, limite, 2):
            if num % i == 0:
                eh_primo = False
                break  

        if eh_primo:
            print(f"O número {num} é primo.")
        else:
            print(f"O número {num} não é primo.")

