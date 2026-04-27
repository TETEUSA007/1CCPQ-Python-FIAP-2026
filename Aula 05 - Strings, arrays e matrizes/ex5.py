# Exercício 5

nomes = []

while True:
    nome = input("Digite um nome: ")

    if nome == "":
        break

    nomes.append(nome)

print("\nNomes na ordem inversa:")

for i in range(len(nomes) - 1, -1, -1):
    print(nomes[i])