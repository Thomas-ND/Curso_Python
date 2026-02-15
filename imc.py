while True:
    try:
            peso = float(input("Digite o seu peso em kg: "))
            altura = float(input("Digite a sua altura em metros: "))
            
            imc = peso/(altura**2)
            imc = round(imc, 2)

            if imc <18.5:
                   print("Você está abaixo do peso")
            elif imc >= 18.5 and imc <=24.99:
                   print("Você está no nível de peso normal")
            elif imc >= 25 and imc <= 29.99:
                   print("Você está obeso")
            else:
                   print("Você está com obesidade grave")
            break
    except ValueError:
            print("Valor inválido! Digite um valor aceitável")