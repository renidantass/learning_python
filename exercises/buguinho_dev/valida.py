# coding:utf-8
""" Módulo para validação de dados """

class Validar:
    def __init__(self):
        pass

    def nome(self, nome):
        if len(nome.split(' ')) >= 2:
            return nome
        else:
            return self.nome(raw_input('Digite o seu nome completo: '))

    def senha(self, senha):
        if len(senha) > 3:
            return senha
        else:
            return self.senha(raw_input('Digite a senha: '))

    def agencia(self, agencia):
        if len(agencia) > 1 and len(agencia) < 4:
            return agencia
        else:
            return self.agencia(raw_input('Digite o número da agência: '))

    def conta(self, conta):
        if len(conta) > 1 and len(conta) < 4:
            return conta
        else:
            return self.conta(raw_input('Digite o número da conta: '))