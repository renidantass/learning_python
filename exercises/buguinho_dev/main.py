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
        v = Validar()
        listar_opcoes()
        try:
            tmp = int(raw_input('Banco <<< '))
        except ValueError:
            print 'Digite apenas números'
        if tmp == 1:
            agencia = v.agencia(raw_input('Digite o número da agência: '))
            conta = v.conta(raw_input('Digite o número da conta: '))
            with Client(agencia, conta) as cliente:
                esc = 0
                while esc != 6:
                    try:
                        esc = int(raw_input('[1] - Consultar saldo\n[2] - Extrato\n[3] - Transferir\n[4] - Depositar'
                                        '\n[5] - Depositar em outra conta\n[6] - Saque\n[7] - Sair\n: '))
                    except ValueError:
                        print  'Informe uma opção válida\n'
                    if esc == 1:
                        cliente.consultar_saldo()
                    elif esc == 2:
                        cliente.emitir_extrato()
                    elif esc == 3:
                        d_agencia = v.agencia(raw_input('Digite o número da agência: '))
                        d_conta = v.conta(raw_input('Digite o número da conta: '))
                        cliente.transferir(d_agencia, d_conta)
                    elif esc == 4:
                        cliente.depositar()
                    elif esc == 5:
                        d_agencia = v.agencia(raw_input('Digite o número da agência: '))
                        d_conta = v.conta(raw_input('Digite o número da conta: '))
                        cliente.depositar_em_outra(d_agencia, d_conta)
                    elif esc == 6:
                        cliente.sacar()
                    elif esc == 7:
                        exit(0)
                    else:
                        print 'Opção inválida'
        elif tmp == 2:
            nome = v.nome(raw_input('Digite o seu nome completo: '))
            senha = v.senha(raw_input('Digite a senha: '))
            agencia = v.agencia(raw_input('Digite o número da agência: '))
            conta = v.conta(raw_input('Digite o número da conta: '))
            with Client() as cliente:
                print cliente.criar_usuario(nome, senha, agencia, conta)
        elif tmp == 3:
            exit(0)

if __name__ == '__main__':
    menu()