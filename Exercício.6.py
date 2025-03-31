def main():
    # Solicita ao usuário a quantidade de dias, horas, minutos e segundos
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))

    # Calcula o total em segundos
    total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

    # Exibe o resultado
    print(f"O total em segundos é {total_segundos}.")


# Executa o programa
if __name__ == "__main__":
    main()