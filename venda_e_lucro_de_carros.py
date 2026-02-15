while True:
    try:
        print("Esta é uma calculadora para ver o lucro ou prejuizo em vendas de carros.")
        ci = True
        while ci == True:
            cifrao = input("Primeiramente, digite o cifão da moeda usada: ")
            if not any(char.isdigit() for char in cifrao):
                break
            else:
                print("Digite apenas letras e simbolos.")

        compra = float(input("Digite o valor da compra do carro: "))
        investimento = float(input("Digite o valor do investimento no carro: "))
        venda = float(input("Digite o valor da venda: "))

        valor_total = venda - (compra + investimento)
        if valor_total > 0:
            print(f"Você teve um lucro de: {cifrao} {valor_total}")
            break
        if valor_total < 0:
            print(f"Você teve um prejuizo de: {cifrao} {valor_total}")
            break
        else:
            print("Não teve nem prejuizo e nem lucro.")
            break
    except ValueError:
        print("Você digitou um valor inválido! Tente novamento do começo.")
        

