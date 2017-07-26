# coding:utf-8
"""
    Exercício proposto por: https://github.com/BugginhoDeveloper/mini-projeto-4-python
    Página BugginhoDeveloper
    Resumo:
        Crie um aplicativo em console que simule o funcionamento básico de um caixa eletrônico
"""
from valida import Validar
from banco import Client


def listar_opcoes():
    print '''\n[1] - Acessar conta\n[2] - Criar conta\n[3] - Sair'''

def menu():
    tmp = ''
    while tmp != 'exit':
        listar_opcoes()
        tmp = int(raw_input('Banco <<< '))
        if tmp == 1:
            pass
        elif tmp == 2:
            v = Validar()
            nome = v.nome(raw_input('Digite o seu nome completo: '))
            senha = v.senha(raw_input('Digite a senha: '))
            agencia = v.agencia(raw_input('Digite o número da agência: '))
            conta = v.conta(raw_input('Digite o número da conta: '))
            with Client() as cliente:
                print cliente.criar_usuario(nome, senha, agencia, conta)
        elif tmp == 3:
            exit(1)

if __name__ == '__main__':
    menu()