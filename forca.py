def jogar():
    print("*********************************")
    print("*** Bem-vindo ao jogo da Forca! ***")
    print("*********************************")
    
    palavra_secreta = "yamal".upper()
    letras_acertadas = ["_"] * len(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0 
    
    while not enforcou and not acertou:
        print(" ".join(letras_acertadas))  # Mostra as letras acertadas até agora
        chute = input("Qual é a letra? ")
        chute = chute.strip().upper()
        
        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1 
            print(f"Você errou! Tentativas restantes: {10 - erros}")
        
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas  # Verifica se todas as letras foram acertadas

    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print("Você perdeu, seu burro! A palavra era:", palavra_secreta)
        
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()