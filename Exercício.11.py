def main():
    # Solicita ao usuário a quantidade de km percorridos e dias alugados
    km_percorridos = float(input("Digite a quantidade de km percorridos: "))
    dias_alugados = int(input("Digite a quantidade de dias alugados: "))

    # Define os valores das tarifas
    preco_por_dia = 60.0
    preco_por_km = 0.15

    # Calcula o preço total
    total_a_pagar = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

    # Exibe o resultado
    print(f"O total a pagar pelo aluguel do carro é R$ {total_a_pagar:.2f}.")


# Executa o programa
if __name__ == "__main__":
    main()
