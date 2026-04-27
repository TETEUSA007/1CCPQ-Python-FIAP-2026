# Exercício 8 - Soma de Matrizes

linhas = int(input("Quantas linhas terá a matriz? "))
colunas = int(input("Quantas colunas terá a matriz? "))

matriz_a = []
matriz_b = []
matriz_soma = []

print("\nDigite os valores da matriz A")

for i in range(linhas):
    linha = []

    for j in range(colunas):
        valor = int(input(f"A[{i}][{j}]: "))
        linha.append(valor)

    matriz_a.append(linha)

print("\nDigite os valores da matriz B")

for i in range(linhas):
    linha = []

    for j in range(colunas):
        valor = int(input(f"B[{i}][{j}]: "))
        linha.append(valor)

    matriz_b.append(linha)

for i in range(linhas):
    linha = []

    for j in range(colunas):
        soma = matriz_a[i][j] + matriz_b[i][j]
        linha.append(soma)

    matriz_soma.append(linha)

print("\nResultado da soma das matrizes:")

for linha in matriz_soma:
    print(linha)