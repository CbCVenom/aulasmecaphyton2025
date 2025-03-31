def main():
    # Solicita ao usuário o preço da mercadoria e a porcentagem de desconto
    preco = float(input("Digite o preço da mercadoria: "))
    desconto_percentual = float(input("Digite o percentual de desconto: "))

    # Calcula o valor do desconto e o preço final
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto

    # Exibe o resultado
    print(f"O valor do desconto foi de R$ {desconto:.2f}.")
    print(f"O preço a pagar é R$ {preco_final:.2f}.")


# Executa o programa
if __name__ == "__main__":
    main()
