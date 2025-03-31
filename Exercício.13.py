def main():
    # Solicita o salário do funcionário
    salario = float(input("Digite o salário do funcionário: "))

    # Calcula o novo salário com reajuste de 35%
    reajuste = salario * 0.35
    novo_salario = salario + reajuste

    # Exibe o resultado
    print(f"O novo salário com reajuste de 35% é R$ {novo_salario:.2f}.")


# Executa o programa
if __name__ == "__main__":
    main()