chances = 6
letrasJogadas = []
ganhou = False

resposta = input("Digite a resposta: ").upper().split()[:1:][0]  # Retorna a primeira palavra em string
letraResposta = list(resposta)  # Retorna um array com cada letra separada
quantLetra = len(resposta)
letrasAcertadas = ['_' for _ in range(quantLetra)]  # Lista para armazenar letras acertadas

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while not ganhou and chances > 0:
    print("Palavra: ", ' '.join(letrasAcertadas))
    pergunta = input("Digite uma letra: ").upper()
    
    if pergunta in letrasJogadas:
        print("\nVocê já jogou essa letra. Tente outra.")
        continue
    
    letrasJogadas.append(pergunta)
    
    if pergunta in letraResposta:
        print("\nAcertou!")
        for i in range(quantLetra):
            if letraResposta[i] == pergunta:
                letrasAcertadas[i] = pergunta
    else:
        print(f"\nErrou! Chances restantes: {chances}")
        chances -= 1
    
    if '_' not in letrasAcertadas:
        ganhou = True
        print("Parabéns! Você ganhou!")
    elif chances == 0:
        print(f"Você perdeu! A palavra era: {resposta.capitalize()}")
