nota_matematica = int(input("Digite a nota de matemática: "))
nota_portugues = int(input("Digite a nota de português: "))
nota_historia = int(input("Digite a nota de história: "))
nota_geografia = int(input("Digite a nota de geografia: "))

media = (nota_matematica + nota_portugues + nota_historia + nota_geografia ) / 4

print("Sua média foi: ", media)

if media >= 7:
    print("Você está aprovado!")
    if media < 7 and media >= 5:
        print("Você está de recuperação!")
        if media < 5:
            print("Você está reprovado!")