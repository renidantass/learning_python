# coding:utf-8

pt = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
total, cont = 0, 1
mais, termo = 10, pt
while mais != 0:
    total += mais
    while cont <= total:
        print '{} ->'.format(termo),
        termo += r
        cont += 1
    print 'PAUSA'
    mais = input("Quantos termos a mais você quer mostrar? ")
