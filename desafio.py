menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
quantidade_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Informe o valor de depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += "\n" + " Depósito ".center(14, "#") + "\n"
            extrato += f"(+) {valor_deposito:.2f} \n"
            print("Depósito concluído!")

        else:
            print("O valor de depósito não pode ser negativo!")

    elif opcao == "s":
        print("Saque")
        if quantidade_saques <= LIMITE_SAQUES:
            valor_saque = float(input("Informe o valor de saque: "))
            if valor_saque <= limite:
                if valor_saque <= saldo and valor_saque > 0:
                    saldo -= valor_saque
                    extrato += "\n" + " Saque ".center(14, "#") + "\n"
                    extrato += f"(-) {valor_saque:.2f} \n"
                    quantidade_saques += 1
                    print("Saque concluído!")
                else:
                    print("Não possível realizar o saque por falta de saldo ou valor negativo!")
            else:
                print("Não possível realizar o saque acima de 500.00")       
        else:
            print("Quantidade saques diários excedida!")
    
    elif opcao == "e":
        print(" Extrato ".center(30, "="))
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\n\nSaldo: R$ {saldo:.2f}")
        print("=".center(30, "="))

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")