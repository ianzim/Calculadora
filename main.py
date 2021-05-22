from math import *
from random import *
from numpy import * 
from mat_basica import *
from geom import *
import os
from an_combin import *
unidades = ('km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm')


operations_types = ('MATEMÁTICA BÁSICA', 'GEOMETRIA',
                    'ANÁLISE COMBINATÓRIA')

mat_basica = ('SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO',
              'DIVISÃO', 'POTENCIAÇÃO', 'RADICIAÇÃO', 'FÓRMULA DE BÁSKHARA')
geom = ('DADOS DE CÍRCULOS', 'DADOS DE CILINDROS',
        'DADOS DE PIRÂMIDES REGULARES', 'DADOS DE CONES', 'DADOS DE CUBOS', 'DADOS DE ESFERAS')
analise_comb = ('FATORIAL', 'COMBINAÇÃO', 'ARRANJO',
                'COMBINAÇÃO COMPLETA', 'PERMUTAÇÃO COM REPETIÇÃO', 'DESARRANJO')
#func = ('PRIMEIRO GRAU', 'SEGUNDO GRAU')


def cabec(txt):
    print()
    print('-' * 35)
    print(f'{txt:^35}')
    print('-' * 35)
    print()

def get_option(tupla):
    for i, v in enumerate(tupla):
        print(f'OPÇÃO [{i}]..... {v}')
    global opção
    opção = int(input('Digite sua opção: '))
    while opção > len(tupla) - 1 or opção < 0:
        opção = int(input('OPÇÃO INVÁLIDA... Digite sua opção: '))

    return opção

def main():

    cabec('ESCOLHA A ÁREA')
    area = get_option(operations_types)
    if area == 0:  # MATEMÁTICA BÁSICA
        cabec('ESCOLHA A OPERAÇÃO')
        op = get_option(mat_basica)
        if op == 0:
            print(soma())

        elif op == 1:
            print(subt())

        elif op == 2:
            print(mult())

        elif op == 3:
            print(div())

        elif op == 4:
            print(pot())

        elif op == 5:
            print(rad())
        
        elif op == 6:
            print(baskhara())

    elif area == 1: # GEOMETRIA
        cabec('ESCOLHA A UNIDADE A SER USADA')
        unid = get_option(unidades)
        cabec('ESCOLHA O DADO')
        op = get_option(geom)
        if op == 0:
            print(f'{circ()}{unidades[unid]}')

        elif op == 1:
            print(f'{cil()}{unidades[unid]}')

        elif op == 2:
            print(f'{pir()}{unidades[unid]}')

        elif op == 3:
            print(f'{cone()}{unidades[unid]}')

        elif op == 4:
            print(f'{cubo()}{unidades[unid]}')

        elif op == 5:
            print(f'{esf()}{unidades[unid]}')

    elif area == 2: # ANÁLISE COMBINATÓRIA
        cabec('ESCOLHA A OPERAÇÃO')
        op = get_option(analise_comb)

        if op == 0:
            print(fat())
        
        elif op == 1:
            print(comb())
        
        elif op == 2:
            print(arr())

        elif op == 3:
            print(combComp())

        elif op == 4:
            print(permRept())
        
        elif op == 5:
            print(desarr())

    # elif area == 3: # FUNÇÕES
    #     print("EM DESENVOLVIMENTO")



while True:
    main()
    print()
    cont = str(input("Quer continuar? [S/N] ").upper().strip())
    if cont != "S" and cont != "N":
        while cont != "S" and cont != "N":
            cont = str(
                input("OPÇÃO INVÁLIDA!! Quer continuar? [S/N] ").upper().strip())
            if cont in ("SN"):
                break
    if cont == "N":
        break

    if cont == "S":
        os.system('cls' if os.name == 'nt' else 'clear')
    