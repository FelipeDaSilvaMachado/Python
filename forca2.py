import tkinter as tk
import random


def escolher_palavra():
    palavras = ["desenvolvimento", "algoritmo", "logica", "eniac", "etec", "github", "python"]
    return random.choice(palavras).upper()


def atualizar_palavra():
    palavra_label.config(text=" ".join(letras_corretas))


def desenhar_boneco():
    # Desenhar partes do boneco com base no número de tentativas restantes
    if tentativas == 5:
        canvas.create_oval(140, 100, 200, 160)  # Cabeça
    elif tentativas == 4:
        canvas.create_line(170, 160, 170, 290)  # Corpo
    elif tentativas == 3:
        canvas.create_line(170, 190, 140, 240)  # Braço esquerdo
    elif tentativas == 2:
        canvas.create_line(170, 190, 200, 240)  # Braço direito
    elif tentativas == 1:
        canvas.create_line(170, 290, 140, 345)  # Perna esquerda
    elif tentativas == 0:
        canvas.create_line(170, 290, 200, 345)  # Perna direita
        canvas.create_line(117, 140, 222, 180)  # Criando a primeira linha do X da forca
        canvas.create_line(117, 180, 222, 140)  # Criando o segundo linha do X da forca


def verificar_letra():
    global tentativas
    chute = letra_entry.get().upper()
    letra_entry.delete(0, tk.END)

    if len(chute) != 1 or not chute.isalpha():
        resultado_label.config(text="Digite uma única letra válida.")
        return

    if chute in letras_corretas or chute in letras_erradas:
        resultado_label.config(text="Você já tentou essa letra. Tente outra.")
        return

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_corretas[i] = letra
        resultado_label.config(text="Boa! A letra está na palavra.")
    else:
        tentativas -= 1
        letras_erradas.append(chute)
        desenhar_boneco()
        resultado_label.config(text="A letra não está na palavra.")

    atualizar_palavra()

    if "_" not in letras_corretas:
        resultado_label.config(text="Parabéns! Você adivinhou a palavra!")
        letra_entry.config(state=tk.DISABLED)
    elif tentativas == 0:
        resultado_label.config(
            text=f"Você perdeu! A palavra era: {palavra_secreta}")
        letra_entry.config(state=tk.DISABLED)


# Inicializa o jogo
palavra_secreta = escolher_palavra()
letras_corretas = ["_" for _ in palavra_secreta]
tentativas = 6
letras_erradas = []

# Configura a interface gráfica
root = tk.Tk()
root.title("Jogo da Forca")

canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()
canvas.create_line(5, 400, 5, 50)
canvas.create_line(5, 50, 170, 50)
canvas.create_line(170, 50, 170, 100)

palavra_label = tk.Label(root, text=" ".join(
    letras_corretas), font=("Helvetica", 18))
palavra_label.pack(pady=20)

letra_entry = tk.Entry(root, font=("Helvetica", 16))
letra_entry.pack()

verificar_button = tk.Button(root, text="Verificar", command=verificar_letra)
verificar_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
resultado_label.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()