"""
Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde
você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
posição está livre. Verifique também quando um jogador venceu a partida.
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual
cada elemento é outra lista também com três elementos.
"""
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

jogador = 'X'

while True:
    print("\n  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(tabuleiro[i])}")
    print(f"\nJogador {jogador}, é sua vez.")

    while True:
        try:
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida. Digite números de 0 a 2.")
            continue
        
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Jogada inválida. As coordenadas devem estar entre 0 e 2.")
            continue
        if tabuleiro[linha][coluna] != ' ':
            print("Jogada inválida. Esta posição já está ocupada.")
            continue
        
        tabuleiro[linha][coluna] = jogador
        break

    if ((tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador) or
        (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador) or
        any(all(tabuleiro[i][j] == jogador for j in range(3)) for i in range(3)) or
        any(all(tabuleiro[i][j] == jogador for i in range(3)) for j in range(3))):
        print("\n  0 1 2")
        for i in range(3):
            print(f"{i} {' '.join(tabuleiro[i])}")
        print(f"\nParabéns! Jogador {jogador} venceu!")
        break

    if all(' ' not in linha for linha in tabuleiro):
        print("\n  0 1 2")
        for i in range(3):
            print(f"{i} {' '.join(tabuleiro[i])}")
        print("\nEmpate!")
        break

    jogador = 'O' if jogador == 'X' else 'X'
