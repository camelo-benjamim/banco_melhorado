import random


class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0.0

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
    def __init__(self, numConta):
        ##instanciei a superclasse e criei um novo atributo que é o bonus acomulado
        super().__init__(numConta)
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
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num
    
    def criarContaBonificada(self):
        num = random.randint(0,1000)
        b = ContaBonificada(num)
        self.contas.append(b)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

    ##adicionei o método render bônus a classe Banco
    def renderBonus(self,numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i,ContaBonificada):
                i.renderBonus()
                return True
        return False
