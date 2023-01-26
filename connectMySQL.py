import mysql.connector as connector

class Connector:
    def __init__(self):
        self._db = connector.connect(
            host=' db4free.net',
            port=3306,
            user='benjamim',
            passwd='neinpasswort88',
            db='db_contas'
        )
        self._cursor = self._db.cursor()
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS CONTA(ID INT PRIMARY KEY NOT NULL, SALDO REAL NOT NULL, POUPANCA INT NOT NULL, BONIFICADA INT NOT NULL);''')
    
    def criarConta(self,id,is_poupanca,is_bonificada,saldo):
        self._cursor.execute('''INSERT INTO CONTA  (ID,SALDO,POUPANCA,BONIFICADA) VALUES ({},{},{},{});'''.format(str(id),str(saldo),str(is_poupanca),str(is_bonificada)))
        self._db.commit()
    
    def movimentarFinanceira(self,saldo,id):
        try:
            self._cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
            self._db.commit()
            print("movimentação realizada com sucesso! ")
            return saldo
        except :
            return("Erro no banco de dados!")
        

    def consultarSaldo(self,id):
        try:
            conta = self._cursor.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
            resultado = self._cursor.fetchall()[0]
            saldo = resultado[1]
            return saldo
        except:
            return("Conta não encontrada! ")

    def retornarContaPoupanca(self,id):
        conta = self._cursor.execute('''SELECT * FROM CONTA WHERE ID={} AND POUPANCA=1'''.format(str(id)))
        try:
            resultado =  self._cursor.fetchall()[0]
            return resultado
        except:
            return -1
    def retornarContaBonificada(self,id):
        conta = self._cursor.execute('''SELECT * FROM CONTA WHERE ID={} AND BONIFICADA=1'''.format(str(id)))
        try:
            resultado =  self._cursor.fetchall()[0]
            return resultado
        except:
            return -1
    def rendimentoPoupanca(self,id,saldo):
        self._cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self._db.commit()

    def rendimentoBonificada(self,id,saldo):
        self._cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self._db.commit()

    def verificarExistencia(self,id):
        conta = self._cursor.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
        try:
            resultado = self._cursor.fetchall()[0]
            return resultado
        except Exception as erro:
            print(erro)
            return -1
    def close(self):
        self._db.close()
    
