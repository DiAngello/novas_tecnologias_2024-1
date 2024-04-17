"""
6. Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do
segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.

"""
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta > 0:
    sqrt_delta = delta ** 0.5
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)
    print(f"Raiz x': {x1}")
    print(f"Raiz x'': {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Raiz x': {x}")
    print(f"Raiz x'': {x}")
else:
    print("Não foi possível calcular as raízes.")

