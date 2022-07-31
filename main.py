from ctypes import util
from utils import menu
import operacoes

class calculadoraSimples:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.opc = 0
        self.qtdItensMenu = 0

    def Iniciar(self):
        menu(0, 'CALCULADORA SIMPLES')
        while True:
            try:
                self.n1 = int(input('Digite o primeiro valor: '))
                self.opcoes()
                if self.opc == 5:
                    self.operação()
                    break
                while True:
                    try:
                        self.n2 = int(input('Digite o segundo valor: '))
                        break
                    except:
                        print('Digite um valor inteiro!')
                break        
            except:
                print('Digite um valor inteiro!')
        self.operação()

    def opcoes(self):
        self.qtdItensMenu = menu(1, 'Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Raiz Quadrada')
        while True:
            try:
                self.opc = int(input('Opção: '))
                break
            except:
                print('Digite um valor inteiro!')

    def operação(self):
        while True:
            if 0 < self.opc <= self.qtdItensMenu+1:
                if self.opc == 1:
                    print(f'Soma: {operacoes.som(self.n1, self.n2)}')
                if self.opc == 2:
                    print(f'Subtração: {operacoes.sub(self.n1, self.n2)}')
                if self.opc == 3:
                    print(f'Multiplicação: {operacoes.mul(self.n1, self.n2)}')
                if self.opc == 4:
                    print(f'Divisão: {operacoes.div(self.n1, self.n2)}')
                if self.opc == 5:
                    #t2 = menu(0, 'RAIZ DE:', str(self.n1), str(self.n2))
                    print(f'Raiz Quarada: {operacoes.sqrt(self.n1 if op == 1 else self.n2)}')
                    return
                    """while True:
                        op = int(input('OPÇÃO: '))
                        if 0 < op <= t2:
                            print(f'Raiz Quarada: {operacoes.sqrt(self.n1 if op == 1 else self.n2)}')
                            break
                        else: 
                            print('Valor incorreto!')"""
            op = input('Fazer outra operação? [S/N]: ').capitalize().strip()
            if op[0] in 'Nn':
                print('Até logo!')
                break
            else:
                self.qtdItensMenu= menu(1, 'Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Raiz Quadrada')
            while True:
                try:
                    self.opc = int(input('Opção: '))
                    break
                except:
                    print('Digite um valor inteiro!')

calc1 = calculadoraSimples()
calc1.Iniciar()