def menu ():
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novos Usuários
[7] Sair
=> """
return imput (textwrap.dedent(menu))


def deposita (saldo, valor, extrato, /):
    if valor > 0:
       saldo += valor
       extrato += f"Deposito: R$ {valor:.2f}"
        print("----DEPOSITO REALIZADO COM SUCESSO!----")
    else:
        print("----VALOR INVALIDO----")

return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque , limite_saque):
    if excedeu_saldo:
        print("Saldo Insulficiente")
    elif excedeu_limite:
        print("Saque foi Excedido")
    elif excedeu_saques:
        print("O saque maximo foi Excedido")
    elif valor > 0:
        saldo -= valor
        extrato += "Saque: R$ {valor:.2f} /n"
        numero_saque ++ 1
        print("Saque Realizado com Sucesso!")

    else:
        print("O valor é invalido")

    return saldo, extrato

def exibir_extrato (saldo, /, extrato):

def criar_usuario(usuarios):
    cpf = input(Informe o CPF(somente numeros): *)
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("O usuario já existe com esse CPF:  *")
    return

    nome = input(Informe o nome completo: *)
    data_nascimento = input(Informe a data de nascimento(dd-mm-aaaa): *)
    endereco = input(Informe o endereco(logradouro, nro - bairro - cidade/sigla estado): *)

usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados =  [usuario for usuario in usuarios if usuario["cpf" == cpf]
    return  usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(agencia, numero_conta, usuarios):
    cpf = input("Inform o CPF do usário")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("---conta criada com sucesso!----")
        return{"agencia": agencia, "numero_conta: numero_conta, "usuario": usuario}

    print("Usuário não encontrado, digitação incorreta!") 
def listar_contas(contas):
    for conta in contas:
        linha + f***\
            agência:/t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
   ***
    print('*'+ 100)
    print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

while True:

    opcao = input(menu)
f opcao == "1":
        valor = obter_valor("Informe o valor do depósito: ")             
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = obter_valor("Informe o valor do saque: ")
        saldo, extrato, numero_saques, saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
            saques=saques,
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "3":
        exibir_historico_saques(saques)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "5":
        listar_contas(contas)

    elif opcao == "7":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
   
