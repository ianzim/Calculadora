from math import *

circulo = ['CIRCUNFERÊNCIA', 'ARCO', 'ÁREA', 'SETOR CIRCULAR', 'ÂNGULO CENTRAL', 'COROA CIRCULAR']
cilindro = ['ALTURA', 'RAIO', 'VOLUME', 'ÁREA TOTAL', 'ÁREA LATERAL']
piram = ['ALTURA', 'ÁREA TOTAL', 'VOLUME', 'VOLUME DO TRONCO']
con = ['ALTURA', 'ÁREA TOTAL', 'GERATRIZ', 'VOLUME', 'ÁREA LATERAL']
cub = ['MEDIDA DO LADO', 'VOLUME', 'DIAGONAL INTERNA', 'DIAGONAL DA FACE']
esfera = ['ÁREA DA SUPERFÍCIE', 'VOLUME', 'ÁREA DA SUPERFÍCIE DA SEMIESFERA', 'VOLUME DA SEMIESFERA']

def get_option(tupla):
    for i, v in enumerate(tupla):
        print(f'OPÇÃO [{i}]..... {v}')
    global opção
    opção = int(input('Digite sua opção: '))
    while opção > len(tupla) - 1 or opção < 0:
        opção = int(input('OPÇÃO INVÁLIDA... Digite sua opção: '))

    return opção

def cabec(txt):
    print()
    print('-' * 35)
    print(f'{txt:^35}')
    print('-' * 35)
    print()

def circ():
    cabec('ESCOLHA O DADO DO CÍRCULO')
    op = get_option(circulo)
    if op == 0:
        r = float(input('Raio: '))
        return f'RESULTADO: {2*pi*r:.2f}'
    
    elif op == 1:
        a = float(input('Ângulo do arco em graus: '))
        r = float(input('Raio: '))
        return f'RESULTADO: {(a/360)*(2*pi*r):.2f}'
    
    elif op == 2:
        r = float(input('Raio: '))
        return f'RESULTADO: {pi*(r**2):.2f}'

    elif op == 3:
        a = float(input('Ângulo do setor em graus: '))
        r = float(input('Raio: '))
        return f'RESULTADO: {(a/360)*(pi*(r**2)):.2f}'

    elif op == 4:
        dado = str(input(('Irá informar arco (A) ou setor circular (S)? '))).lower()
        if dado == 's':
            s = float(input('Área do setor: '))
            r = float(input('Raio: '))
            return f'RESULTADO: {(360*s)/(pi*(r**2)):.2f}'

        elif dado == 'a':
            a = float(input('Arco: '))
            r = float(input('Raio: '))
            return f'RESULTADO: {(180*a)/(pi*r):.2f}'
    
    elif op == 5:
        R = float(input('Raio da circunferência maior: '))
        r = float(input('Raio da circunferência menor: '))
        A = pi * (R**2)
        a = pi * (r**2)
        return f'RESULTADO: {(A - a):.2f}'

def cil(): 
    cabec('ESCOLHA O DADO DO CILINDRO')
    op = get_option(cilindro)
    if op == 0:
        v = float(input('Volume do cilindro: '))
        r = float(input('Raio da base: '))
        return f'RESULTADO {v/(pi*(r**2)):.2f}'

    elif op == 1:
        v = float(input('Volume do cilindro: '))
        h = float(input('Altura do cilindro: '))
        return f'RESULTADO: {(v/(pi*h))**(1/2):.2f}'

    elif op == 2:
        r = float(input('Raio da base: '))
        h = float(input('Altura do cilindro: '))
        return f'RESULTADO: {pi*(r**2)*h:.2f}'

    elif op == 3:
        r = float(input('Raio do cilindro: '))
        h = float(input('Altura do cilindro: '))
        ab = pi*(r**2)
        al = 2*pi*r*h

        return f'RESULTADO: {2*ab + al:.2f}'

    elif op == 4:
        r = float(input('Raio do cilindro: '))
        h = float(input('Altura do cilindro: '))
        return f'RESULTADO: {2*pi*r*h:.2f}'

def pir():
    cabec("ESCOLHA O DADO DA PIRÂMIDE")
    op = get_option(piram)
    if op == 0:
        v = float(input('Volume da pirâmide: '))
        ab = float(input('Área da base: '))
        return f'RESULTADO: {3*v/ab:.2f}'
    
    elif op == 1:
        n = int(input("Números de lados da base: "))
        l = float(input("Medida do lado: "))
        p = n*l
        h = float(input("Altura da pirâmide: "))
        
        if n == 3:
            ab = ((l**2) * sqrt(3)) / 4 

        elif n == 4:
            ab = l**2
        
        elif n == 5:
            ang = radians(54)
            t = tan(ang)
            a = l*t/2
            ab = 5*(l*a/2)
        
        elif n == 6:
            ab = 6*(((l**2) * sqrt(3)) / 4) 

        else: 
            ab = float(input("Área de base: "))
      
        return f'RESULTADO: {(p*h/2) + ab:.2f}'
        
    elif op == 2:
        h = float(input('Altura da pirâmide: '))
        ab = float(input('Área da base: '))
        return f'RESULTADO: {ab*h/3:.2f}'
    
    elif op == 3:
        H = float(input('Altura da pirâmide original: '))
        A = float(input('Área da base da pirâmide original: '))
        h = float(input('Altura da pirâmide cortada: '))
        k = h/H
        a = (k**2) * A
        V = A*H/3
        v = a*h/3
        return f'RESULTADO: {V-v:.2f} '

def cone(): 
    cabec("ESCOLHA O DADO DO CONE: ")
    op = get_option(con)
    if op == 0:
        r = float(input("Área da base: "))
        v = float(input("Volume do cone: "))
        return f'RESULTADO: {(3*v)/(pi*(r**2)):.2f}'
    
    elif op == 1:
        g = float(input("Geratriz: "))
        r = float(input("Raio da base: "))
        return f'RESULTADO: {((pi*(r**3))/g) + pi*r**2:.2f}'
    
    elif op == 2:
        r = float(input("Raio da base: "))
        a = float(input("Ângulo da planificação do cone: "))
        return f'RESULTADO: {(a/360)*r:.2f}'

    elif op == 3:
        r = float(input("Raio da base: "))
        h = float(input("Altura: "))
        return f'RESULTADO: {(pi*(r**2)*h)/3:.2f}'

    elif op == 4:
        g = float(input("Geratriz: "))
        r = float(input("Raio da base: "))
        return f'RESULTADO: {(pi*(r**3))/g:.2f}'
        
def cubo(): 

    cabec("ESCOLHA O DADO DO CUBO: ")
    op = get_option(cub)
    if op == 1:
        v = float(input("Digite o volume do cubo: "))
        return f'RESULTADO: {v**(1/3):.2f}'
    
    elif op == 2:
        l = float(input("Digite a medida do lado: "))
        return f'RESULTADO: {l**3:.2f}'

    elif op == 3:
        l = float(input("Digite a medida do lado: "))
        return f'RESULTADO: {l*sqrt(3):.2f}'

    elif op == 4:
        l = float(input("Digite a medida do lado: "))
        return f"RESULTADO: {l*sqrt(2):.2f}"

def esf(): 
    cabec("ESCOLHA O DADO DA ESFERA: ")
    op = get_option(esfera)

    if op == 0: 
        r = float(input('Digite o raio da esfera: '))
        return f'RESULTADO: {4*pi*(r**2):.2f}'
    
    elif op == 1: 
        r = float(input('Digite o raio da esfera: '))
        return f'RESULTADO: {4/3*pi*(r**3):.2f}'

    elif op == 2: 
        r = float(input('Digite o raio da esfera: '))
        return f'RESULTADO: {2*pi*(r**2):.2f}'

    elif op == 3:
        r = float(input('Digite o raio da esfera: '))
        return f'RESULTADO: {4/6*pi*(r**3):.2f}'