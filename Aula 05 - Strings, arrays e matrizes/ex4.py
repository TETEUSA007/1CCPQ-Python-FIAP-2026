# Exercício 4

n = int(input("Digite o tamanho do vetor: "))

vetor = []
soma = 0

for i in range(n):
    numero = int(input(f"Digite o número da posição {i}: "))
    vetor.append(numero)

for i in range(n):
    soma = soma + vetor[i]

print("\nVetor:")
print(vetor)

print("Somatória dos números:", soma)