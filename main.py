from ctypes import util
from utils import menu
import operacoes

class calculadoraSimples:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def Iniciar(self):
        menu(0, 'CALCULADORA SIMPLES')
        while True:
            try:
                self.n1 = int(input('Digite o primeiro valor: '))
                while True:
                    try:
                        self.n2 = int(input('Digite o segundo valor: '))
                        break
                    except:
                        print('Digite um valor inteiro!')
                break        
            except:
                print('Digite um valor inteiro!')

        qtd = menu(1, 'Soma', 'Subtração', 'Multiplicação', 'Divisão')

        while True:
            while True:
                try:
                    res = int(input('Opção: '))
                    break
                except:
                    print('Digite um valor inteiro!')
            if 0 < res <= qtd+1:
                if res == 1:
                    print(f'Soma: {operacoes.som(self.n1, self.n2)}')
                if res == 2:
                    print(f'Subtração: {operacoes.sub(self.n1, self.n2)}')
                if res == 3:
                    print(f'Multiplicação: {operacoes.mul(self.n1, self.n2)}')
                if res == 4:
                    print(f'Divisão: {operacoes.div(self.n1, self.n2)}')
            op = input('Fazer outra operação? [S/N]: ').capitalize().strip()
            if op[0] in 'Nn':
                print('Até logo!')
                break

calc1 = calculadoraSimples()
calc1.Iniciar()