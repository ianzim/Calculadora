import math

def soma():
    print()
    s = 0
    quant = int(input('Quantos números quer somar? '))
    for cont in range(quant):
        s += float(input(f'{cont + 1}º número: '))
    return f'RESULTADO: {s}'

def subt():
    print()
    inicial = float(input('Digite o número inicial: '))
    sub = float(input(f"{inicial} - "))
    return f'RESULTADO: {inicial - sub}'

def mult():
    print()
    print("OBS: A MULTIPLICAÇÃO SERÁ FEITA DA FORMA: AxBxCx... = Z")
    print()
    quant = int(input('Quantos números serão multiplicados? '))
    for c in range(quant):
        if c == 0:
            a = float(input('1º Número: '))
        else:
            a *= float(input(f'{c + 1}º Número: '))

    return f'RESULTADO: {a}'

def div():
    print()
    n = float(input('Numerador: '))
    d = float(input('Denominador: '))

    return f'RESULTADO: {(n/d)}'

def pot():
    print()
    b = float(input('Base: '))
    exp = float(input('Expoente: '))

    return f'RESULTADO: {(b**exp)}'

def rad():
    print()
    i = float(input('Índice da raíz: '))
    r = float(input('Radical: '))

    return f'RESULTADO: {(r**(1/i))}'

def baskhara():
    print()
    a = int(input('A = '))
    b = int(input('B = '))
    c = int(input('C = '))

    delta = (b**2 - (4 * a * c))
    rD = delta**(1/2)

    x1 = (-b + rD) / (2*a)
    x2 = (-b - rD) / (2*a)

    if rD < 0:
        return 'A RAÍZ DE DELTA É NEGATIVA'

    else:
        return f'X1 = {x1:.5f}\nX2 = {x2:.5f}'