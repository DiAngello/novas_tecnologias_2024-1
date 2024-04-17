"""
Faça um jogo da Forca utilizando listas. Dada uma palavra, dê algumas
chances para o usuário acertar.

"""
palavra_chave = "Banana"
palavra = ['__'] * len(palavra_chave)

acertou = False
enforcou = False
erros = 0

while not acertou and not enforcou:
    chute = input("Digite uma letra: ").upper() 
    
    if chute in palavra_chave.upper():  
        for i in range(len(palavra_chave)):
            if chute == palavra_chave[i].upper():
                palavra[i] = chute  
    
    else:
        erros += 1  

    acertou = '__' not in palavra  
    enforcou = erros == 5  

    print(' '.join(palavra))  

if acertou:
    print("Parabéns, você acertou a palavra!")
else:
    print("Você foi enforcado! A palavra correta era:", palavra_chave)
