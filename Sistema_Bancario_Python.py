menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do Depósito: "))
           
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou")

    elif opcao == "s":
        valor = float(input("Valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_quantidade_de_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Invalida, Saldo insuficente!")

        elif excedeu_limite:
            print("Operação Invalida, Limite de saque excedido!")

        elif excedeu_quantidade_de_saques:
            print("Operação Invalida, Quantidade limite de saques alcançada!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("O valor informado não é valido")

    elif opcao == "e":

        """---------------EXTRATO---------------"""

        print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")

        """---------------EXTRATO---------------"""

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione a operação desejada")