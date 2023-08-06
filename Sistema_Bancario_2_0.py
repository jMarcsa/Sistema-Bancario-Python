
def menu():
    menu = """\n
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova_conta
    [nu]Novo_usuario
    [q]Sair
    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada")
        else:
            print("Operação Falhou")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
            
            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_quantidade_de_saques = numero_saques >= limite_saques

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

            return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
       
        print("---------------EXTRATO---------------")

        print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")

        print("-------------------------------------")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
         print("\n Usuario já existente")
         return
    
    nome= input("Nome Completo:")
    data_de_nascimento = input("Data de Nascimento: ")
    endereço = input("Informe o endereço (logradouro, nº - bairro - cidade/estado(sigla))")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereço})
    print("Cadastro Realizado!!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("CPF DO USUARIO:  ")  
   usuario = filtrar_usuario(cpf, usuarios)
   if usuario:
        print("\nConta criada")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   else:
            print("\n Conta não cadastrada")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 1
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA= "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do Depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do Saque: "))

            saldo, extrato = sacar(

            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,

            )

        elif opcao == "e":

            exibir_extrato(saldo, extrato=exibir_extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":

            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione a operação desejada")

main()