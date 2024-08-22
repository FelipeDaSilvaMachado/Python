# The comment `# This Python code snippet prompts the user to input three numbers, `num1`, `num2`, and
# `num3`. It then compares these numbers to determine their order and prints a message indicating the
# order of the numbers.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))

if num1 >= num2 >= num3:
    print(f"A ordem é: {num3} 'num3', {num2} 'num2', {num1} 'num1'.")
elif num1 >= num2 <= num3 and num1 >= num3:
    print(f"A ordem é: {num2} 'num2', {num3} 'num3', {num1} 'num1'.")
elif num1 <= num2 >= num3 and num1 <= num3:
    print(f"A ordem é: {num1} 'num1', {num3} 'num3', {num2} 'num2'.")
elif num1 >= num2 <= num3 and num3 >= num1:
    print(f"A ordem é: {num2} 'num2', {num1} 'num1', {num3} 'num3'.")
elif num1 <= num2 >= num3 and num3 <= num1:
    print(f"A ordem é: {num3} 'num3', {num1} 'num1', {num2} 'num2'.")
else:
    print(f"A ordem é: {num1} 'num1', {num2} 'num2', {num3} 'num3'.")
