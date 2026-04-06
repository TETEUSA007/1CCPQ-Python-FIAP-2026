def boas_vindas(nome):
    print(f"Ola, {nome}!! Seja bem-vindo")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    return num_a + num_b

resultado_soma = soma(1, 2)
print(resultado_soma)