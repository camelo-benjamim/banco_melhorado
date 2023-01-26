import sqlite3

class Connect_db:
    def __init__(self):
        ##tornando método privado para não ser acessado fora da classe (similar ao java!)
        self._con = sqlite3.connect('banco.db')
        self._con.execute('''CREATE TABLE IF NOT EXISTS CONTA(ID INT PRIMARY KEY NOT NULL, SALDO REAL NOT NULL, POUPANCA INT NOT NULL, BONIFICADA INT NOT NULL);''')
    
    def close(self):
        self._con.close()

    def criarConta(self,id,is_poupanca,is_bonificada,saldo):
        self._con.execute('''INSERT INTO CONTA  (ID,SALDO,POUPANCA,BONIFICADA) VALUES ({},{},{},{});'''.format(str(id),str(saldo),str(is_poupanca),str(is_bonificada)))
        self._con.commit()
    
    def movimentarFinanceira(self,saldo,id):
        try:
            self._con.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
            self._con.commit()
            print("movimentação realizada com sucesso! ")
            return saldo
        except :
            return("Erro no banco de dados!")
        

    def consultarSaldo(self,id):
        try:
            conta = self._con.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
            resultado = conta.fetchall()[0]
            saldo = resultado[1]
            return saldo
        except:
            return("Conta não encontrada! ")

    def retornarContaPoupanca(self,id):
        conta = self._con.execute('''SELECT * FROM CONTA WHERE ID={} AND POUPANCA=1'''.format(str(id)))
        try:
            resultado =  conta.fetchall()[0]
            return resultado
        except:
            return -1
    def retornarContaBonificada(self,id):
        conta = self._con.execute('''SELECT * FROM CONTA WHERE ID={} AND BONIFICADA=1'''.format(str(id)))
        try:
            resultado =  conta.fetchall()[0]
            return resultado
        except:
            return -1
    def rendimentoPoupanca(self,id,saldo):
        self._con.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self._con.commit()

    def rendimentoBonificada(self,id,saldo):
        self._con.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self._con.commit()

    def verificarExistencia(self,id):
        conta = self._con.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
        try:
            resultado =  conta.fetchall()[0]
            return resultado
        except:
            return -1





        
    
    
    

