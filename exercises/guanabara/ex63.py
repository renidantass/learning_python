# coding:utf-8
n_termos = int(input("Quantos termos você quer mostrar? "))

t1, t2 = 0, 1
cont = 3
while cont <= n_termos:
    t3 = t1 + t2
    print '{} -> {} ->'.format(t1, t2),
    t1 = t2
    t2 = t3
    cont += 1
