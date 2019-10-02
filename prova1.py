#Nome: Mateus Trajano Gouvea de Souza
#Data: 02/10/2019
#Descrição: Prova 1 redigida

def raizes(a, b, c):
    delta = (b*b) - (4*a*c)
    x1 = 0
    x2 = 0
    from math import sqrt
    if delta >= 0:
        if delta == 0:
            x1 = -b/2*a
            x2 = x1
        
        else:
            x1 = (-b+sqrt(delta))/2*a
            x2 = (-b-sqrt(delta))/2*a

        print('Raiz 1= ',x1)
        print('Raiz 2= ', x2)
        return 0
    else:
        delta = -delta
        x1 = str(-b/2*a)+'+'+str(sqrt(delta)/2*a)+'i'
        x2 = str(-b/2*a)+'-'+str(sqrt(delta)/2*a)+'i'
        print('Raiz 1= ',x1)
        print('Raiz 2= ',x2)
        return 1

def main1():
    a = int(input('Entre com o coeficiente a'))
    b = int(input('Entre com o coeficiente b'))
    C = int(input('Entre com o coeficiente c'))
    resultado = raizes(a, b, c)
    if resultado == 0:
        print('Como delta é positivo: ',resultado)
    else:
        print('Como delta é negativo: ',resultado)

def pi():
    b = -1
    a = -1/b
    c = -1/(b-2)
    cont = 1
    diferenca = a-c
    serie_infinita = 0
    while diferenca >= 5*(10**-8):
        if cont % 2 != 0:
            serie_infinita += a
        else:
            serie_infita += -a
        cont +=1
        b += -2

    pi = 4*serie_infinita
    print (pi)


def nob(num_a, num_b):
    dezena_num_a = num_a // 10
    unidade_num_a = num_a % 10
    resposta1 = ''
    dezena_num_b = num_b // 10
    unidade_num_b = num_b % 10
    resposta = 0
    if (num_a >= 100 or num_b >= 100):
        return resposta1
    else:
        resposta = dezena_num_a + dezena_num_b + unidade_num_a + unidade_num_b
        return resposta

def main2():
    valor1 = int(input('Entre com o primeiro valor(limite é 99)'))
    valor2 = int(input('Entre com o segundo valor(limite é 99)'))
    resposta = nob(valor1, valor2)
    if resposta == '':
        print('Você digiou um valor acima do limite')
    else:
        print('O numero esperado é: ',resposta)


