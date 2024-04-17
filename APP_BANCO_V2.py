menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta

[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

def funcao_deposito(saldo, valor, extrato):
    
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def funcao_saque(*, saldo, valor, extrato, limite, LIMITE_SAQUES):
    
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def funcao_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (Apenas números): ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n # # Usuario já criado com este CPF # #")
        return
    
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd - mm - aaaa): ")
    endereco = input("Informe seu indereço (rua, numero - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print (" * * Usuário criado com sucesso * * ")

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF (Apenas números): ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n * * Conta criada com sucesso * * ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n # # Usuário não encontrado # # ")

while True:
    opcao = input(menu)
    
    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = funcao_deposito(saldo, valor, extrato)

    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))  

        saldo, extrato = funcao_saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            umero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )
    
    elif opcao == "e":
        funcao_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta  = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
