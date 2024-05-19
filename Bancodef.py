saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
contas = []
Agencia = '0001'
clientes = []

def menu():
    print('-' * 28 + '\nOlá, bem-vindo ao BANCO DIO!!\n' + '-' * 28)
    opcao = int(input('Escolha a opção que deseja: \n Para Depósito pressione: (1) \n Para Saque pressione:    (2) \n Para Extrato pressione:  (3) \n Cadastrar Usuário:       (4)\n Criar conta:             (5)\n Listar contas:           (6)\n Para Sair pressione:     (7)\n' + '-' * 28 + '\n Informe a opção: '))
    return opcao

def deposito(saldo, /):
    print('-' * 10 + ' Depósito ' + '-' * 10)
    valor_deposito = float(input("Informe o valor do seu depósito: R$ "))
    if valor_deposito > 0:
        saldo += valor_deposito
        print('-' * 28 + f'\nSeu depósito de R$ {valor_deposito:.2f} foi realizado com sucesso!\n' + '-' * 28)
    else:
        print('-' * 28 + '\nNão podemos realizar este tipo de operação!\n' + '-' * 28)
    return saldo

def saque(*, saldo, numero_saques, limite, limite_saques):
    print('-' * 10 + ' Saque ' + '-' * 10)
    if numero_saques >= limite_saques:
        print('Você atingiu o limite diário de saques.')
    else:
        valor_saque = float(input('Informe o valor que deseja retirar: R$ '))
        if valor_saque > saldo:
            print('Desculpe, não poderemos realizar essa operação. Seu saldo é insuficiente\n' + '-' * 28 + f'\nSaldo Atual de R$ {saldo:.2f}')
        elif valor_saque > limite:
            print('Desculpe, o valor do saque excede o limite permitido.\n' + '-' * 28 + f'\nLimite de saque: R$ {limite:.2f}')
        else:
            saldo -= valor_saque
            numero_saques += 1
            print('-' * 28 + f'\nSaque de R$ {valor_saque:.2f} realizado com sucesso!\n' + '-' * 28)
    return saldo, numero_saques

def extrato(saldo, limite, /, *, numero_saques, limite_saques):
    print('-' * 10 + " Extrato " + '-' * 10)
    print(f'Saldo atual: R$ {saldo:.2f}')
    print(f'Limite de saque por transação: R$ {limite:.2f}')
    print(f'Número de saques realizados hoje: {numero_saques}')
    print(f'Número máximo de saques diários: {limite_saques}')

def cadastrar_usuario(clientes):
    cpf = input('Informe o CPF (somente número): ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('-' * 28 + '\n Já existe usuário com esse CPF!\n')
    else:    
        nome = input('Informe o nome completo: ')
        data_nasc = input('Informe a data de nascimento (dia-mês-ano): ')
        end = input('Informe o endereço (logradouro, número, bairro, cidade/estado): ')

        clientes.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'end': end})

        print('-' * 28 + '\nCadastro criado com sucesso\n')

def criar_conta(agencia, numero_conta, clientes):
    cpf = input('Informe o CPF do Cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('-' * 28 + '\nConta Criada com sucesso\n' + '-' * 28)
        return {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': cliente}
    else:
        print('-' * 28 + '\nCliente não encontrado, fluxo de criação de conta finalizada\n')
        return None

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente['cpf'] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f'''Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['cliente']['nome']}
'''
        print(linha)

while True:
    opcao = menu()
    
    if opcao == 1:
        saldo = deposito(saldo)
    elif opcao == 2:
        saldo, numero_saques = saque(saldo=saldo, numero_saques=numero_saques, limite=limite, limite_saques=limite_saques)
    elif opcao == 3:
        extrato(saldo, limite, numero_saques=numero_saques, limite_saques=limite_saques)
    elif opcao == 4:
        cadastrar_usuario(clientes)
    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(Agencia, numero_conta, clientes)

        if conta:
            contas.append(conta)
    elif opcao == 6:
        listar_contas(contas)
    elif opcao == 7:
        print('Obrigado por utilizar nossos serviços.')
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
