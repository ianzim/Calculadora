from math import *

def fat():
    n = int(input("Digite o número: "))

    return f"RESULTADO: {factorial(n)}"

def comb():
    n = int(input("Digite o total de elementos: "))
    p = int(input("Digite a partição dos elementos: "))

    if p > n:
        while p > n:
            p = int(input("A PARTIÇÃO NÃO PODE SER MAIOR QUE O TOTAL DE ELEMENTOS! Digite a partição dos elementos: "))

    num = factorial(n)
    den = factorial(p) * factorial(n-p)
    c = num/den

    return f'RESULTADO: {int(c)}'

def arr():
    n = int(input("Digite o total de elementos: "))
    p = int(input("Digite a partição dos elementos: "))

    if p > n:
        while p > n:
            p = int(input("A PARTIÇÃO NÃO PODE SER MAIOR QUE O TOTAL DE ELEMENTOS! Digite a partição dos elementos: "))

    a = factorial(n)/factorial(n-p)
    return f'RESULTADO: {int(a)}'

def combComp():
    return "MAIS DIFÍCIL E EU NÃO PROGRAMEI AINDA. FAÇA NA MÃO rsrs"

def permRept():
    total = 1
    n = int(input("Digite o total de elementos: "))
    q = int(input("Quantos elementos se repetem? "))

    for i in range(q):
        m = int(input(f"Número de repetições do {i+1}º elemento: "))
        total *= factorial(m)
    
    r = factorial(n)/total
    return f'RESULTADO: {int(r)}'

def desarr():
    v = 0
    n = int(input("Dessaranjo de quantos elementos? "))
    
    for i in range(n+1):
        v += factorial(n) * (((-1)**i)/factorial(i))
    
    return(v)