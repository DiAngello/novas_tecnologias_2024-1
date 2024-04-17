"""
2. Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um
losango utilizando asteriscos (*).

"""
print("Caixa:")
for i in range(5):
    print("*********")

print("\nOval:")
print("  *****")
print(" *******")
for i in range(3):
    print("*********")
print(" *******")
print("  *****")


print("\nSeta:")
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))
print("  ***")
print("  ***")

print("\nLosango:")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

