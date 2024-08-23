palavra = "python"
letras_usuario = []
chances = 4
ganhou = False
while True:
    # criar a nossa logica
    for letra in palavra:
        if letra.upper() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")

    letras_usuario.append(tentativa.upper())
    
    if tentativa.upper() not in palavra.upper():
        chances -= 1
    if tentativa.upper() in palavra.upper() == palavra.upper():
        print("Essa letra já foi digitada.")
        chances -= 1
    else:
        ganhou = True
    
    for letra in palavra:
        if letra.upper() not in letras_usuario:
            ganhou = False
    
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
