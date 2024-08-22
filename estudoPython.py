lista = []  # Inicializa a lista vazia
num = int(input("Digite um número: "))

# Sempre que eu quiser manipular uma lista vazia recebendo dados do usuario eu utilizo o atributo 'append'
lista.append(num)

# Solicita mais cinco ou mais números dependendo de quanto for parametrizado
for contador in range(5):  # Itera quantas vezes for parametrizado para pedir mais números
    num = int(input("Digite outro numero: "))
    lista.append(num)

# Exibe a lista em ordem ordenada e reversa
print("Lista ordenada: ", sorted(lista))
print("Lista reversa: ", sorted(lista, reverse=True))