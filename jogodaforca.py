# Constante para o número inicial de chances
CHANCES_INICIAIS = 6

# Função para exibir o enforcado de acordo com o número de chances restantes
def exibir_enforcado(chances_restantes):
    estados = [
        '''
        -----
        |   |
        |   
        |   
        |   
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |   
        |   
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |   |
        |   
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|
        |   
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |   
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  /
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        -----
        '''
    ]
    print(estados[CHANCES_INICIAIS - chances_restantes])

# Função para exibir o cabeçalho do jogo
def exibir_cabecalho():
    print("\n" + "="*30)
    print("       JOGO DA FORCA")
    print("="*30 + "\n")

# Função para exibir a palavra com letras acertadas
def exibir_palavra(letras_acertadas):
    print("Palavra: ", ' '.join(letras_acertadas))

# Função para "limpar" o console com múltiplas linhas
def limpar_console():
    print("\n" * 50)

# Função principal do jogo
def jogar_forca():
    chances_restantes = CHANCES_INICIAIS
    letras_jogadas = []
    ganhou = False

    exibir_cabecalho()
    
    resposta = input("Digite a resposta: ").upper().strip()
    letra_resposta = list(resposta)
    quant_letra = len(resposta)
    letras_acertadas = ['_' for _ in range(quant_letra)]  # Lista para armazenar letras acertadas

    while not ganhou and chances_restantes > 0:
        limpar_console()  # Limpa o console simulando uma nova tela
        exibir_palavra(letras_acertadas)
        exibir_enforcado(chances_restantes)
        
        # Exibe a quantidade de chances restantes
        print(f"\nChances restantes: {chances_restantes}")

        pergunta = input("Digite uma letra: ").upper().strip()

        # Verifica se a entrada é apenas uma letra
        if not pergunta.isalpha() or len(pergunta) == 0:
            print("\nApenas letras são permitidas. Tente novamente.")
            continue

        # Usa apenas o primeiro caractere se mais de um for digitado
        pergunta = pergunta[0]

        if pergunta in letras_jogadas:
            print("\nVocê já jogou essa letra. Tente outra.")
            continue

        letras_jogadas.append(pergunta)
        
        if pergunta in letra_resposta:
            print("\nAcertou!")
            for i in range(quant_letra):
                if letra_resposta[i] == pergunta:
                    letras_acertadas[i] = pergunta
        else:
            print(f"\nErrou! Chances restantes: {chances_restantes - 1}")
            chances_restantes -= 1
        
        if '_' not in letras_acertadas:
            ganhou = True
        elif chances_restantes == 0:
            limpar_console()  # Limpa o console antes de mostrar o resultado final
            exibir_palavra(letras_acertadas)
            exibir_enforcado(chances_restantes)
            print(f"\nVocê perdeu! A palavra era: {resposta.capitalize()}")
            print(f"\nVocê teve {CHANCES_INICIAIS - chances_restantes} tentativa(s) restante(s).")
            return  # Sai da função após o jogo terminar

    # Se o jogador ganhou
    limpar_console()  # Limpa o console antes de mostrar o resultado final
    exibir_palavra(letras_acertadas)
    exibir_enforcado(chances_restantes)
    print(f"\nParabéns! Você ganhou!")
    print(f"\nVocê teve {chances_restantes} tentativa(s) restante(s).")

# Inicia o jogo
jogar_forca()
