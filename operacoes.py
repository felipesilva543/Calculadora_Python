from asyncio.windows_events import NULL
import math
from pickle import NONE
# from icecream import ic

def som(a=0, b=0):
    """
    -> Soma de números
    param a: Primeiro termo da soma
    param b: Segundo termo da soma
    return: A soma de a e b (a + b)
    """
    return a + b

def sub(a=0, b=0):
    """
    -> Subtração de números
    param a: Primeiro termo da subtração
    param b: Segundo termo da subtração
    return: A subtração de a por b (a - b)
    """
    return a - b

def mul(a=0, b=0):
    """
    -> Multiplicação de números
    param a: Multiplicando
    param b: Multiplicador
    return: A multiplicação de a por b (a * b)
    """
    return a * b

def div(a=0, b=1):
    """
    -> Divisão de números
    param a: Dividendo
    param b: Divisor
    return: A divisão de a por b (a / b)
    """
    while True:
        try:
            return a / b
        except:
            print('Operação inválida! Não é possível dividir por 0 (zero).')
            return NONE

def sqrt(a=0):
    """
    -> Raiz quadrada de um número
    param a: Valor para pegar raiz quadrada
    return : Valor da raiz quadrada de a
    """
    return math.sqrt(a)