# Exercício 6

n = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(n):
    letra = input(f"Digite o caractere da posição {i}: ")
    vetor.append(letra)

print("\nVetor original:")
print(vetor)

inicio = 0
fim = n - 1

while inicio < fim:
    temp = vetor[inicio]
    vetor[inicio] = vetor[fim]
    vetor[fim] = temp

    inicio += 1
    fim -= 1

print("\nVetor invertido:")
print(vetor)