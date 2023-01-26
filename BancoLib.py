import random
from connect import Connect_db

class Conta():
    def __init__(self, numConta,saldo):
        self.numero = numConta
        self.saldo = saldo

    def deposite(self, valor):
        ##Desconto de 1% no valor depositado
        self.saldo = self.saldo + valor - 0.001*valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - float(valor)
            return True
        else:
            return False


class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.01
##Conta bonificada é uma classe filha de Conta
class ContaBonificada(Conta):
    def __init__(self, numConta,saldo):
        ##instanciei a superclasse e criei um novo atributo que é o bonus acomulado
        super().__init__(numConta,saldo)
        self.bonus_acomulado = 0.00
    
    def deposite(self, valor):
        super().deposite(valor)
        self.bonus_acomulado += valor * 0.0001
    
    def renderBonus(self):
        ## o bônus será passado em valor para a conta do usuário
        ## para isso adicionarei o bonus ao saldo da conta no formato salario += bonus
        self.saldo += self.bonus_acomulado
        self.bonus_acomulado = 0.00

class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.connect = Connect_db()

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num,0.0)
        self.connect.criarConta(c.numero,0,0,c.saldo)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num,0.0)
        self.connect.criarConta(p.numero,1,0,p.saldo)
        return num
    
    def criarContaBonificada(self):
        num = random.randint(0,1000)
        b = ContaBonificada(num,0.0)
        self.connect.criarConta(b.numero,0,1,b.saldo)
        return num

    def consultaSaldo(self, numConta):
        x = self.connect.verificarExistencia(numConta)
        if x == -1:
            return "A conta não existe..."
        else:
            saldo = x[1]
            return saldo

    def depositar(self, numConta, valor):
        conta = self.connect.verificarExistencia(numConta)
        if conta == -1:
            return "A conta não existe...."
        else:
            saldo = conta[1]
            conta = Conta(numConta,saldo)
            conta.deposite(float(valor))
            saldo = conta.saldo
            self.connect.movimentarFinanceira(saldo,numConta)

    def sacar(self, numConta, valor):
        conta = self.connect.verificarExistencia(numConta)
        if conta == -1:
            return "A conta não existe...."
        else:
            saldo = conta[1]
            conta = Conta(numConta,saldo)
            autorizado = conta.sacar(valor)
            if autorizado == False:
                print("Saque não permitido, valor do saquei maior do que o saldo")
            else:
                self.connect.movimentarFinanceira(conta.saldo,numConta)
                return conta.saldo
    def renderPoupanca(self, numConta):
        saldo = self.consultaSaldo(numConta)
        conta_poupanca = self.connect.retornarContaPoupanca(numConta)
        if conta_poupanca == -1:
            print("Erro, a conta poupança digitada acima não existe...")
        else:
            p = Poupanca(numConta,saldo)
            p.render()
            saldo = p.saldo
            self.connect.rendimentoPoupanca(numConta,saldo)
            return saldo
    ##adicionei o método render bônus a classe Banco
    def renderBonus(self,numConta):
        saldo = self.connect.consultarSaldo(numConta)
        conta_bonificada = self.connect.retornarContaBonificada(numConta)
        if conta_bonificada == -1:
            print("Erro, a conta bonificada digitada acima não existe...")
        else:
            b = ContaBonificada(numConta,saldo)
            b.renderBonus()
            saldo = b.saldo
            self.connect.rendimentoBonificada(numConta,saldo)
            return saldo

