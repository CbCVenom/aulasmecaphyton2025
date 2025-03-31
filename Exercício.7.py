def main():
    # Solicita ao usuário o salário e a porcentagem de aumento
    salario = float(input("Digite o salário atual: "))
    porcentagem = float(input("Digite a porcentagem de aumento: "))

    # Calcula o valor do aumento e o novo salário
    aumento = salario * (porcentagem / 100)
    novo_salario = salario + aumento

    # Exibe o resultado
    print(f"O aumento foi de R$ {aumento:.2f}.")
    print(f"O novo salário é R$ {novo_salario:.2f}.")


# Executa o programa
if __name__ == "__main__":
    main()
