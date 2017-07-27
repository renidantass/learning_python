# coding:utf-8
"""
    Módulo por parte do cliente para o programa do banco Bugginho
"""
from time import strftime
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
            if len(r) == 0:
                print 'Usuário não cadastrado'
            else:
                return r[0]
        except Exception as e:
            raise Exception(e)

    def __enter__(self):
        """ Método para usá-lo com with """
        self.__logar()
        try:
            print '\nBanco informa: {} logou-se no sistema'.format(self.__user[1])
        except Exception as e:
            pass
        finally:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Mesma coisa do acima :p """
        self.__conn.close() # Certificando-se de fechar a conexão do db
        print '\nBanco informa: {} desconectou-se'.format(self.__user[1])

    def __logar(self):
        """ Método para verificar a senha do usuário """
        __senha = self.__user[2]
        senha = raw_input('Digite a sua senha: ')
        while senha != __senha:
            print 'Senha incorreta!'
            senha = raw_input('Digite a sua senha: ')

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
        print "Saldo do usuário: R${:.2f}\n".format(self.__user[5])

    def emitir_extrato(self):
        """ Emite o extrato do usuário se o mesmo quiser """
        try:
            user_id = self.__user[0]
            results = self.__cur.execute('''SELECT * FROM transacoes WHERE client_id={}'''.format(user_id)).fetchall()
            if len(results) >= 1:
                for r in results:
                    print 'Há uma ação com valor de R${:.2f} envolvendo você\n'.format(r[3])
            else:
                print 'Você ainda não tem transações realizadas\n'
        except Exception as e:
            pass
    
    def transferir(self, agencia, conta):
        """ Transferir dinheiro de uma conta para outra """
        try:
            saldo_atual, user_id = self.__user[5], self.__user[0]
            r = self.__cur.execute('''SELECT * FROM contas WHERE agencia = {} AND conta = {}'''.format(agencia, conta)).fetchall()[0]
            saldo_atual_dest, id_dest = r[5], r[0]
            valor = float(raw_input('Digite o valor a transferir: R$'))
            tmp = raw_input('Deseja transferir R${:.2f} para {}? (S/N) '.format(valor, r[1])).upper()
            if tmp == 'S':
                if valor > saldo_atual:
                    print 'Você não tem dinheiro suficiente para essa transferência'
                else:
                    saldo_atual -= valor
                    saldo_atual_dest += valor
                    print "Valor do usuário atual agora R${:.2f}, valor do outro usuário agora {:.2f}".format(saldo_atual, saldo_atual_dest)
                    self.__cur.execute('''UPDATE contas SET saldo = {} where id = {}'''.format(saldo_atual, self.__user[0]))
                    self.__cur.execute('''UPDATE contas SET saldo = {} WHERE id = {}'''.format(saldo_atual_dest, r[0]))
                    self.__cur.execute('''INSERT INTO transacoes (client_id, destination_id, value, data) 
                                                    VALUES(?, ?, ?, ?)''', (user_id, id_dest, valor, strftime('%d/%m/%y')))
                    self.__conn.commit()
                    self.__user = self.__checar_usuario()
                    print 'Valor transferido com sucesso!\n'
            elif tmp == 'N':
                print 'OK! Não iremos transferir nenhuma quantia a esta conta'
            else:
                print 'Opção inválida'
        except Exception as e:
            raise Exception(e)
    
    def depositar(self):
        """ Depositar dinheiro na conta """
        try:
            saldo_atual = self.__user[5]
            valor = float(raw_input('Quanto você deseja depositar? R$'))
            tmp = raw_input('Deseja depositar R${:.2f} nesta conta de {}? (S/N) '.format(valor, self.__user[1])).upper()
            if tmp == 'S':
                saldo_atual += valor
                self.__cur.execute('''UPDATE contas SET saldo = {} WHERE id = {}'''.format(saldo_atual, self.__user[0]))
                self.__cur.execute('''INSERT INTO transacoes (client_id, destination_id, value, data)
                                                            VALUES(?, ?, ?, ?)''', (self.__user[0],
                                                                                    self.__user[0],
                                                                                    valor,
                                                                                    strftime('%d/%m/%y')))
                self.__conn.commit()
                self.__user = self.__checar_usuario()
                print 'Depósito feito com sucesso!\n'
            elif tmp == 'N':
                print 'OK! Não iremos depositar nenhuma quantia nesta conta'
            else:
                print 'Opção inválida'
        except Exception as e:
            raise Exception(e)

    def depositar_em_outra(self, agencia, conta):
        """ Depositar dinheiro em oura conta """
        try:
            r = self.__cur.execute('''SELECT * FROM contas WHERE agencia = {} AND conta = {}'''.format(agencia, conta)).fetchall()[0]
            user_id, id_dest, saldo_atual = self.__user[0], r[0], r[5]
            valor = float(raw_input('Valor do depósito: R$'))
            tmp = raw_input('Deseja depositar R${:.2f} na conta de {}? (S/N) '.format(valor, r[1])).upper()
            if tmp == 'S':
                saldo_atual += valor
                self.__cur.execute('''UPDATE contas SET saldo = {} WHERE id = {}'''.format(valor, id_dest))
                self.__cur.execute('''INSERT INTO transacoes (client_id, destination_id, value, data)
                                                        VALUES(?, ?, ?, ?)''', (user_id, id_dest, valor, strftime('%d/%m/%y')))
                self.__conn.commit()
                print 'Depósito feito com sucesso!\n'
            elif tmp == 'N':
                print 'OK! Não iremos depositar nenhuma quantia na conta'
            else:
                print 'Opção inválida'
        except Exception as e:
            raise Exception(e)

    def sacar(self):
        """ Sacar dinheiro da conta """
        try:
            saldo_atual = self.__user[5]
            valor = float(raw_input('Digite o valor que deseja sacar: R$'))
            if valor > saldo_atual:
                print 'Você não tem saldo suficiente para sacar'
            else:
                if valor > 1000:
                    print 'Não é permitido sacar mais que R$1000'
                else:
                    try:
                        notas = {100: 0, 50: 0, 20: 0}
                        notas[100] = valor // 100
                        resto = valor % 100
                        notas[50] = resto // 50
                        resto = resto % 50
                        notas[20] = resto // 20
                        print 'Você pode pegar {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 20\n'.format(notas[100], notas[50], notas[20])
                    except Exception as e:
                        raise Exception(e)
        except Exception as e:
            raise Exception(e)
