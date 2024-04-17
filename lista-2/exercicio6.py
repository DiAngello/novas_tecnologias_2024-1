"""
Escreva um programa que controla a utilização das salas de um cinema.
Imagine que a lista lugares_vagos=[10,2,1,3,0] contenha o número de
lugares vagos nas salas 1,2,3,4 e 5, respectivamente. Esse programa lerá o
número da sala e a quantidade de lugares solicitados. Ele deve informar se
é possível vender o número de lugares solicitados, ou seja, se ainda há
lugares livres. Caso seja, possível vender os bilhetes, atualizará o número
de lugares livres. A saída ocorre quando se digita 0 no número da sala.
"""
lugares_vagos = [10, 2, 1, 3, 0]

while True:
    print("Estado atual das salas:")
    for num_sala in range(1, len(lugares_vagos) + 1):
        print(f"Sala {num_sala}: {lugares_vagos[num_sala - 1]} lugares vagos")

    num_sala = int(input("Digite o número da sala (ou 0 para sair): "))

    if num_sala == 0:
        print("Programa encerrado.")
        break

    if num_sala < 1 or num_sala > len(lugares_vagos):
        print("Sala inválida. Tente novamente.")
        continue

    qtd_solicitada = int(input("Digite a quantidade de lugares desejados: "))

    if qtd_solicitada <= lugares_vagos[num_sala - 1]:
        lugares_vagos[num_sala - 1] -= qtd_solicitada
        print(f"{qtd_solicitada} bilhetes vendidos com sucesso para a sala {num_sala}.")
    else:
        print(f"Não há lugares suficientes na sala {num_sala}.")

print("Estado final das salas:")
for num_sala in range(1, len(lugares_vagos) + 1):
    print(f"Sala {num_sala}: {lugares_vagos[num_sala - 1]} lugares vagos")
