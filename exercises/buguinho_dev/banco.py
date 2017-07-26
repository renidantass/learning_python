# coding:utf-8
"""
    Módulo por parte do cliente para o programa do banco Bugginho
"""
import sqlite3


class Client(object):
    def __init__(self, agencia='', conta=''):
        self.agencia = agencia
        self.conta = conta
        self.__conn = sqlite3.connect('banco.db')
        self.__cur = self.__conn.cursor()
        self.__checar_db()
        try:
            self.__user = self.__checar_usuario()
        except Exception as e:
            pass

    def __checar_db(self):
        """ (Checa se)/Cria as tabelas (existem) no arquivo banco.db """
        try:
            self.__cur.execute('''CREATE TABLE contas (id INTEGER PRIMARY KEY,
                                                        nome TEXT NOT NULL,
                                                        senha TEXT NOT NULL,
                                                        agencia INTEGER NOT NULL UNIQUE,
                                                        conta INTEGER NOT NULL UNIQUE, 
                                                        saldo INTEGER DEFAULT 0,
                                                        FOREIGN KEY(id) REFERENCES transacoes(client_id)
                                                        )''')
            self.__cur.execute('''CREATE TABLE transacoes (id INTEGER PRIMARY KEY,
                                                            client_id INTEGER NOT NULL,
                                                            destination_id INTEGER NOT NULL,
                                                            operation_id INTEGER NOT NULL,
                                                            value INTEGER NOT NULL, 
                                                            data TEXT)''')
            self.__conn.commit()
            return 1
        except sqlite3.OperationalError as e:
            return 1
        else:
            return 0

    def __checar_usuario(self):
        """ Método para checar se usuário existe na tabela contas """
        try:
            sql = '''SELECT * FROM contas WHERE agencia = {} AND conta = {}'''.format(self.agencia, self.conta)
            r =  self.__cur.execute(sql).fetchall()
            return r[0] if r else 0
        except Exception as e:
            raise Exception(e)

    def __enter__(self):
        """ Método para usá-lo com with """
        try:
            print '\n{} entrou'.format(self.__user[1])
        except Exception as e:
            pass
        finally:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Mesma coisa do acima :p """
        self.__conn.close() # Certificando-se de fechar a conexão do db

    def criar_usuario(self, nome, senha, agencia, conta):
        """ Método para  criar um usuário na tabela contas do banco.db """
        try:
            self.__cur.execute('''INSERT INTO contas (nome, senha, agencia, conta)
                                                VALUES(?, ?, ?, ?)''', (nome, senha, agencia, conta))
            self.__conn.commit()
            return 1
        except Exception as e:
            raise Exception(e)
        else:
            return 0


    def consultar_saldo(self):
        """ Método para consultar o saldo do usuário """
        print "Saldo do usuário: {}".format(self.__user[5])

    def emitir_extrato(self):
        """ Emite o extrato do usuário se o mesmo quiser """
        pass
    
    def transferir(self):
        """ Transferir dinheiro de uma conta para outra """
        pass
    
    def depositar(self):
        """ Depositar dinheiro na conta """
        pass

    def sacar(self):
        """ Sacar dinheiro da conta """
        pass

