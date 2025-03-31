def main():
    # Solicita ao usuário a temperatura em Celsius
    celsius = float(input("Digite a temperatura em ºC: "))

    # Converte para Fahrenheit
    fahrenheit = ((9 * celsius) / 5) + 32

    # Exibe o resultado
    print(f"A temperatura de {celsius:.2f}ºC equivale a {fahrenheit:.2f}ºF.")


# Executa o programa
if __name__ == "__main__":
    main()
