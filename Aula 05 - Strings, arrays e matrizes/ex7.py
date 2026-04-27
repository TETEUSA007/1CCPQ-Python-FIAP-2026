import random

# Exercício 7 - Matrizes

matriz = []

for i in range(3):
    linha = []

    for j in range(4):
        numero = random.randint(1, 100)
        linha.append(numero)

    matriz.append(linha)

print("Matriz 3x4:\n")

for linha in matriz:
    print(linha)