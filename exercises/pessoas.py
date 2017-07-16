# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def calc_porc(total, chave):
    if chave in ['homens', 'mulheres']:
        return total[chave] / float(total['homens'] + total['mulheres']) * 100
    if chave in ['adultos', 'adolesc']:
        return total[chave] / float(total['adultos'] + total['adolesc']) * 100

def novo_arq(dados, h, m):
    with open('estatisticas.csv', 'a+') as f:
        line = '{},{},{},{}\n' .format(h, m, dados.get('adultos'), dados.get('adolesc'))
        f.write(line)

def main():
    dados = {
        'homens': 0,
        'mulheres' : 0,
        'adultos': 0,
        'adolesc': 0
    }
    with open('pessoas.csv', 'r') as f:
        f.readline()
        for line in f:
            l = line.strip().split(',')
            if int(l[1]) >= 18:
                dados['adultos'] += 1
            elif int(l[1]) < 18:
                dados['adolesc'] += 1
            if l[2] == 'M':
                dados['homens'] += 1
            elif l[2] == 'F':
                dados['mulheres'] += 1
    porc_h, porc_m = calc_porc(dados, 'homens'), calc_porc(dados, 'mulheres')
    print "Porcentagem de homens: %.2f%%" % porc_h
    print "Porcentagem de mulheres: %.2f%%" % porc_m
    print "Quantidade de adultos: %d" % dados['adultos']
    print "Quantidade de adolescentes: %d" % dados['adolesc']
    novo_arq(dados, porc_h, porc_m)

main()