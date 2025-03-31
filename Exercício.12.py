def main():
    # Solicita ao usuário dois valores inteiros
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    # Verifica se a operação é válida (evita divisão por zero)
    if x == y:
        print("Erro: A operação não pode ser realizada pois x - y resulta em zero.")
    else:
        # Calcula o valor de z
        z = ((x ** 2) + (y ** 2)) / ((x - y) ** 2)

        # Exibe o resultado
        print(f"O valor de z é {z:.2f}.")


# Executa o programa
if __name__ == "__main__":
    main()
