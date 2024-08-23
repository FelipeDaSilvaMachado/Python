palavra = "python"
letras_usuario = []
chances = 4
ganhou = False

while True:
    # Mostrar o estado atual da palavra
    for letra in palavra:
        if letra.upper() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nVocê tem {chances} chances")

    while True:
        tentativa = input("Escolha uma letra para adivinhar: ").upper()
        
        # Verificar se a entrada é válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
        elif tentativa in letras_usuario:
            print("Essa letra já foi digitada.")
        else:
            break  # Sai do loop se a entrada for válida

    letras_usuario.append(tentativa)
    
    # Verificar se a letra está na palavra
    if tentativa not in palavra.upper():
        chances -= 1

    # Verificar se o usuário ganhou
    ganhou = True
    for letra in palavra:
        if letra.upper() not in letras_usuario:
            ganhou = False
            break  # Não é necessário continuar se já sabemos que não ganhou

    if chances == 0 or ganhou:
        break

# Mostrar resultado final
if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
