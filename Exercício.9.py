def main():
    # Solicita ao usuário a distância e a velocidade média
    distancia = float(input("Digite a distância a percorrer (em km): "))
    velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))

    # Calcula o tempo de viagem
    tempo_viagem = distancia / velocidade_media

    # Exibe o resultado
    print(f"O tempo estimado de viagem é de {tempo_viagem:.2f} horas.")


# Executa o programa
if __name__ == "__main__":
    main()
