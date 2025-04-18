import textwrap

def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Novo Conta
    [nu] Novo Usuário
    [lc] Listar Contas
    [q] Sair
    
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato,):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques atingido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saque += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato (saldo, *, extrato):
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================================")


def criarusuario(usuarios):
    cpf= input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    if contas:
        for conta in contas:
            print(f"""\n=== Agência: {conta['agencia']} / Conta: {conta['numero_conta']} ===""")
            print(f"""Titular: {conta['usuario']['nome']}""")
    else:
        print("\n@@@ Não existem contas cadastradas! @@@")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao =menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
             saldo = saldo,
             valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saque = numero_de_saques,
            limite_saques = LIMITE_SAQUES
        )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        
        elif opcao == "nc":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            if conta:
                contas.append(conta)
        
        
        elif opcao == "nu":
            criarusuario(usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\n=== Sistema encerrado! ===")
            break
            
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")    

        
if __name__ == "__main__":
    main()




