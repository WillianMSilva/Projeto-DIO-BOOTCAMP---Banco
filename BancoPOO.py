from abc import ABC, abstractmethod
from datetime import date, datetime



# Interface Transacao
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Classe Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Historico
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%s'),

            }


        )

# Classe Conta
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('-'*10+ 'Operação falhou! Você não tem saldo suficiente'+'_'*10)
        elif valor > 0:
            print('-'*10+'Saque realizado com sucesso!'+'-'*10)
            return True
        
        else:
            print('-'*10+'Operação Falhou! Valor informado é inválido.'+'-'*10 )
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo +=valor
            print('-'*10+'Depósito realizado com sucesso!'+'-'*10)
        else:
            print('-'*10+'Operação Falhou! Valor informado é inválido.'+'-'*10 )
            return False
        
        return True

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_limite = numero_saques >= self.limite_saques

        if excedeu_limite:
             print('-'*10+'Operação Falhou! O valor do saque excede o limite.'+'-'*10 )
        elif excedeu_limite:
             print('-'*10+'Operação Falhou! Excedeu o limite de saque diário.'+'-'*10 )
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self) :
        return f"""\
            Agência:\t{self.agencia}
            c\c:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
            """
    
     
        
# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento






# Criando um cliente
cliente = PessoaFisica(
    endereco="Rua das Flores, 123",
    cpf="123.456.789-00",
    nome="João da Silva",
    data_nascimento=date(1985, 5, 15)
)

# Criando uma conta para o cliente
conta = Conta( numero=123456, cliente=cliente)

# Realizando um depósito
conta.depositar(1000.0)
print(f"Saldo após depósito: {conta.saldo}")

# Realizando um saque
if conta.sacar(500.0):
    print(f"Saque realizado com sucesso. Saldo atual: {conta.saldo}")
else:
    print("Saldo insuficiente para saque.")

# Tentando sacar um valor maior que o saldo
if conta.sacar(600.0):
    print(f"Saque realizado com sucesso. Saldo atual: {conta.saldo}")
else:
    print("Saldo insuficiente para saque.")

# Exibindo o histórico de transações
print("Histórico de transações:")
for transacao in conta.historico.transacoes:
    tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
    print(f"{tipo} de R${transacao.valor:.2f}")
