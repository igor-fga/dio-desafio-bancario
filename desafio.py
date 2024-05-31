import textwrap


def menu():
    menu = """\n
    ============ MENU ============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [c]\t Nova conta
    [l]\t Listar contas
    [u]\t Novo usuário
    [q]\t Sair
    
    => """
    return input(textwrap.dedent(menu))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


def sacar(
    *, saldo, valor, extrato, limite, numero_saques, limite_saques
):  # O caracter * para informar que o parametros são passados nomeados

    if numero_saques <= limite_saques:
        if valor <= limite:
            if valor <= saldo and valor > 0:
                saldo -= valor
                extrato += "\n" + " Saque ".center(14, "#") + "\n"
                extrato += f"(-) {valor:.2f} \n"
                numero_saques += 1
                print("Saque concluído!")
            else:
                print(
                    "Não possível realizar o saque por falta de saldo ou valor negativo!"
                )
        else:
            print("Não possível realizar o saque acima de 500.00")
    else:
        print("Quantidade saques diários excedida!")

    return saldo, extrato


def depositar(
    saldo, valor, extrato, /
):  # O caracter / é para informar que os parametros antes dele só pode ser passado por posição

    if valor > 0:
        saldo += valor
        extrato += "\n" + " Depósito ".center(14, "#") + "\n"
        extrato += f"(+) {valor:.2f} \n"
        print("Depósito concluído!")
    else:
        print("O valor de depósito não pode ser negativo!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    print(" Extrato ".center(30, "="))
    print("Não foram realizadas transações." if not extrato else extrato)
    print(f"\n\nSaldo: R$ {saldo:.2f}")
    print("=".center(30, "="))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário com esse CPF já existe!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))


main()
