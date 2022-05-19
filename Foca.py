import random
from tkinter import Y

from regex import R
i = True
tentativas = 0
letras = []
palavras = ["neve","coador","atletismo","cupido","clique","sangue","roseta"]
palavraSecreta = random.choice(palavras)
dica = ["_" for i in palavraSecreta]

def showWord():
    print("Palavra Secreta: ", end="")
    for i in dica:
        print(i,end=" ")
    print()

while i:
    conut = 0
    showWord()
    chute = input("Diga Uma Letra: ")
    while chute not in palavraSecreta:
        showWord()
        chute = input("Essa letra não está na palavra, tento outra: ")
        tentativas+=1
    if chute not in letras:
        letras.append(chute)
        for i in palavraSecreta:
            if chute == i:
                dica[conut] = i
            conut += 1
    else:
        while chute in letras:
            showWord()
            chute = input("Você Ja Tentou Essa Letra, Tente Outra: ")
    if "_" not in dica:
        tentativas += 1
        print(f"Parabens, Você Acertou, a palavras com apenas {tentativas} tentativas, a palavra secreta era: {palavraSecreta}")
        continuar = input("Quer Jogar Denovo: (N/S)")
        if continuar == "S" or continuar == "s":
            palavraSecreta = random.choice(palavras)
            dica = ["_" for i in palavraSecreta]
            letras, tentativas = [],-1
        else:
            print("Adeus")
            i = False

    tentativas += 1
