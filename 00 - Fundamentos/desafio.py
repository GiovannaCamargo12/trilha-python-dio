From abc import ABC, obstractclassmethod, obstractproperty
From datetime import datetime

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


class cliente:
    def__init__(self, endereco)
        self.endereco = endereco
        self.contas = []

     def realizar_trasacao(self, conta, trasacao):
         trasacao.registrar(conta)
      
       def adicionar_conta(self, conta):
           self.contas.append(conta)
 
class pessoaFisica(cliente):
    def__init__(self, nome, data_nascimento, cpf, endereco):
        super().def__init__(enderco) data_nascimento,
            self.nome= nome
            self.data_nascimento =  data_nascimento
            self.cpf = cpf

class conta:
     def__init__(self, numero, clientes):
            self._saldo= 0
            self._numero =  numero
            self._agencia = "0001"
            self._cliente= cliente
            self._historico = historico() 
     @classmethod
      def nova _conta(self, numero, clientes):   
            return cls(numero, clientes)
      @property
      def saldo(self):
              return self.saldo
      @property
      def numero(self):
              return self.numero

      @property
       def numero(self):
          return self.numero

       @property
       def agencia(self):
          return self._agencia

        @property
        def cliente(self):
          return self.cliente

        @property
        def historico(self):
          return self.historico

        def sacar(self):
         self.saldo = self.saldo
         execedeu_saldo = valor > saldo

                if  execedeu_saldo
                    print("Voce não tem saldo suficiente")
                
                elif  valor > 0:
                    self._saldo -= valor
                     print("Saque realizado com sucesso!")

                 else  
                     print("O valor informado é invalido!")

                 return false 
            
          def depositar(self, valor):
                  if valor > 0:
                      self._saldo += valor
                       print("Deposito depositado com sucesso!")
                  else:
                       print("O valor informado é invalido!")
                      return false 
           return true
                    

class contaCorrente(conta):
    def__init__(self, numero, cliente, limite=500, limite_saques=3 ):
        super().__init__(numero, cliente)
        self.limite = limite 
        self.limite_saques =  limite_saques

    def sacar(self, valor):
        numero_saques = len (
        [trasacao for trasacao in self.historico.trasacoes if trasacoes ["tipo"] == saque.__name__] 
        )

        exedeu_limite = valor > self.limite
        exedeu_saques = numero_saques > self.

        if exedeu_limite:
             print("O valor informado exede o limite!")

        elif exedeu_saques:
             print("Exedeu o limite maximo de saques!")
        else:
             return super().sacar(valor)
        return false 

    def __str__(self):
        return f***/
            Agencia:\t{self.agencia}
            C/C:\t{self.numero}
            titular:\t{self.cliente.nome}
        ***
                
   
class historico:
      def__init__(self):
            self>_transacoes = []
      
       @property
       def trasacoes(self):
          return self._trasacoes

       def adicionar_trasacoes(self, trasacao):
           self._trasacoes.append (
                "tipo": trasacoes.__class__.__name__,
                "valor": trasacoes.valor,
                "data": datatime.now()strtime("id-%n-%y %M:%s"),
             )
        

)

           
class trasacao(ABC):
     @property
     @abstrctproperty
     def valor(self):
        pass

    @abstractclassmethod
    def resgistrar(self, conta):
         pass

         

class Saque(trasacao):
    def__init__(self, valor):
        self._valor = valor 

      @property
      def valor(self):
          return self._valor

      def resgistrar(self, conta):
          sucesso_trasacao = conta.sacar(self, sacar)

          if  sucesso_trasacao:
              conta.historico.adicionar_trasacao(self)


class deposito(trasacao):
    def__init__(self, valor):
        self._valor = valor 

      @property
      def valor(self):
          return self._valor

      def resgistrar(self, valor):
          sucesso_deposito = conta.depositar(self, valor)

          if  sucesso_deposito:
              conta.historico.adicionar_deposito(self)

    
