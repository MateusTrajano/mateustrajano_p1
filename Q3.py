#Nome: Mateus Trajano Gouvea de Souza
#Data: 02/10/2019
#Descrição: correção da terceira questão da p1

def pi():
    diferenca = 1
    pi = 0
    i = 1
    j = 1
    while (diferenca > (5*10**(-8))):
        pianterior = pi
        pi = pi + 4/(i*j)
        i += 2
        j *= -1

        diferenca = (pianterior - pi)*j

    print (pi)

pi()
