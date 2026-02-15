print ("Está é uma calculadora de média anual escolar.")
while True:
    try:
        nota1 = float(input("Digite a nota do primeiro trimestre: "))
        nota2 = float(input("Digite a nota do segundo trimestre: "))
        nota3 = float(input("Digite a nota do terceiro trimestre: "))

        media = (nota1 + nota2 + nota3)/3
        media = round(media, 2)

        print(f"A sua média anual é: {media}")
        if media >= 6:
            print("Parabéns, você foi aprovado!")
            break
        elif media <= 5:
            print("Você está reprovado.")
            break
    except ValueError:
        print("Valor inválido! Tente novamente do começo.")