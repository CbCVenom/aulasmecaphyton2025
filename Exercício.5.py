def main():
    # Solicita ao usuário um valor em metros
    metros = float(input("Digite um valor em metros: "))

    # Converte para milímetros
    milimetros = metros * 1000

    # Exibe o resultado
    print(f"{metros} metros equivalem a {milimetros} milímetros.")


# Executa o programa
if __name__ == "__main__":
    main()
