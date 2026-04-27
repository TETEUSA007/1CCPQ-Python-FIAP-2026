import random

# Exercício 1

n = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(n):
    numero = random.uniform(0, 100)
    vetor.append(numero)

print("\nNúmeros gerados:")

for i in range(n):
    print(vetor[i])