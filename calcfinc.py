from math import log


# Calculo de valor futuro
def calcular_valor_futuro():
    capital_inicial = float(input("Digite o valor do capital inicial: "))
    taxa_juros_mensal = float(input("Digite a taxa de juros mensal: "))
    periodo_em_meses = int(input("Digite o período em meses: "))
    
    valor_futuro = capital_inicial * (1 + taxa_juros_mensal) ** periodo_em_meses
    
    return valor_futuro


# Cálculo de capital inicial
def calcular_capital_inicial():
    valor_final = float(input("Digite o valor final: "))
    taxa_juros_mensal = float(input("Digite a taxa de juros mensal: "))
    periodo_em_meses = int(input("Digite o período em meses: "))

    capital_inicial = valor_final / (1 + taxa_juros_mensal) ** periodo_em_meses

    return capital_inicial


# calculo da taxa de juros
def calcular_taxa_juros():
    valor_final = float(input("Digite o valor final: "))
    capital_inicial = float(input("Digite o capital inicial: "))
    periodo_em_meses = int(input("Digite o período em meses: "))

    taxa_juros = (valor_final / capital_inicial) ** (1 / periodo_em_meses) - 1

    return taxa_juros


# calculo de período
def calcular_periodo():
    valor_final = float(input("Digite o valor final: "))
    capital_inicial = float(input("Digite o capital inicial: "))
    taxa_juros_mensal = float(input("Digite a taxa de juros mensal: "))

    periodo = log(valor_final / capital_inicial) / log(1 + taxa_juros_mensal)

    return int(periodo)


# menu
def menu():
    print("O que você gostaria de calcular?\n")
    print("1. Calcular valor futuro (vf)")
    print("2. Calcular capital inicial (ci)")
    print("3. Calcular taxa de juros (i)")
    print("4. Calcular período (t)")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        print("\n Calculando o valor futuro...\n")
        valor_futuro = calcular_valor_futuro()
        print(f"O valor futuro é R${valor_futuro:.2f}")
    
    elif escolha == "2":
        capital_inicial = calcular_capital_inicial()
        print(f"O capital inicial é R${capital_inicial:.2f}")

    elif escolha == "3":
        print("\n Calculando a taxa de juros...\n")
        taxa_juros = calcular_taxa_juros()
        print(f"A taxa de juros é {taxa_juros:.2%}")

    elif escolha == "4":
        print("\n Calculando o período...\n")
        periodo = calcular_periodo()
        print(f"O período é {periodo} meses")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        menu() 


# inicialização
if __name__ == "__main__":
    print("\nBem-vindo à calculadora de Juros Compostos!\n")

    while True:
        menu()
        continuar = input("Deseja calcular algo mais? (s/n): ")
        if continuar.lower() == "n":
            print("\nObrigado por usar a calculadora de Juros Compostos!")
            break
        elif continuar.lower() == "s":
            continue
        else:
            print("opção inválida!\n")
            continue