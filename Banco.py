saldo = 0
Limite = 500
extrato = 0
numero_saques = 0
limite_saques = 3

print( '-'*28 + '\nOlá bem vindo ao BANCO DIO!!\n' + '-'*28)


while True:
    opcao = int(input('Escolha a opção que deseja: \n Para Depósito pressione: (1) \n Para Saque pressione:    (2) \n Para Extrato pressione:  (3) \n Para Sair pressione:     (4)\n' + '-'*28 +'\n Informe a opção: '))
    
    if opcao == 1:
        print('-'*10 + ' Depósito ' + '-'*10)
        deposito = float(input("Informe o valor do Seu Depósito: "))
        if deposito >0:
            saldo += deposito
            print('-' * 28 + f'\nSeu depósito R$ {deposito:.2f}\n' + '-'*28 +'\n Realizado com sucesso')
        else:
            print('-'*28 +'\nNão podemos realizar este tipo de operação!\n'+ '-'*28)
                           
    elif opcao == 2:
        print('-'*10 + ' Saque ' + '-'*10)
        if numero_saques >= limite_saques:
            print('-'*28 + '\nVocê atingiu o limete díario de saques.'+'-'*28)
        
        else:
            saque = float(input('Informe o valor que deseja retirar: R$ '))
            if saque > saldo:
                print('-' * 28 +'\nDesculpe não poderemos realizar essa operação seu Saldo é insuficiente\n' + '-'*28 + f'\nSaldo Atual de {saldo:.2f}')
            elif saque > Limite:
                print('-' * 28 +'\nDesculpe, o valor do saque excede o limite permitido.\n' + '-' * 28 + f'\nLimite de saque: R$ {Limite:.2f}')
            else:
                saldo -= saque
                numero_saques += 1
                print('-' * 28 +f'\nSaque de R$ {saque:.2f} realizado com sucesso!\n' + '-' * 28)
        
    elif opcao == 3:
        print('-' * 10 + ' Extrato ' + '-' * 10)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print(f'Limite de saque: R$ {Limite:.2f}\n' + '-' * 28)
        
    elif opcao == 4:
        print('-' * 28 + '\nObrigado por utilizar nossos serviços.\nBanco Dio\n' + '-' * 28)
        break

    else:
        print('-' * 28 + "\nOperação inválida, por favor selecione novamente a operação desejada.\n" + '-' * 28)