"""
7. Escreva um programa que leia a quantidade em segundos e imprima o
resultado em dias, horas, minutos e segundos.

"""
segundos = int(input("Digite a quantidade de segundos: "))

dias = segundos // (24 * 3600)
segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"Tempo equivalente a {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
