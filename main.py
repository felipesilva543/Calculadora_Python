from utils import menu
import operacoes
from icecream import ic

class calculadoraSimples:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.resOpe = 0
        self.opc = 0
        #self.qtdItensMenu = 0

    def Iniciar(self):
        menu(0, 'CALCULADORA SIMPLES')
        while True:
            try:
                self.n1 = int(input('Digite o primeiro valor: '))
                break
            except:
                print('N1 precisa ser um valor inteiro!')

        while True:
            self.opc, valores = self.opcoes()
            if valores[self.opc-1] == 'SAIR':
                return
            if valores[self.opc-1][0:4:] == 'Raiz':
                self.n1 = self.operação(self.opc)
                self.imprimirResultado(self.n1)
            else:
                while True:
                    try:
                        self.n2 = int(input('Digite o segundo valor: '))
                        break
                    except:
                        print('N2 precisa ser um valor inteiro!')
                self.n1 = self.operação(self.opc)
                self.imprimirResultado(self.n1)

    

    def imprimirResultado(self, res):
        print(f'Resultado: {res}.')

    def opcoes(self):
        qtdItensMenu, valores = menu(1, 'Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Raiz Quadrada', 'SAIR')
        while True:
            try:
                opc = int(input('Opção: '))
                if 0 < opc <= qtdItensMenu+1:
                    return opc, valores
                else:
                    print('Opção inválida!')
            except:
                print('(OPÇÕES) Digite um valor inteiro!')

    def operação(self, operacao):
        if operacao == 1:
            self.resOpe = operacoes.som(self.n1, self.n2)
            return self.resOpe
            print(f'Soma: {self.resOpe}')
        if operacao == 2:
            self.resOpe = operacoes.sub(self.n1, self.n2)
            return self.resOpe
            print(f'Subtração: {self.resOpe}')
        if operacao == 3:
            self.resOpe = operacoes.mul(self.n1, self.n2)
            return self.resOpe
            print(f'Multiplicação: {self.resOpe}')
        if operacao == 4:
            self.resOpe = operacoes.div(self.n1, self.n2)
            return self.resOpe
            print(f'Divisão: {self.resOpe}')
        if operacao == 5:
            self.resOpe = operacoes.sqrt(self.n1)
            return self.resOpe
            print(f'Raiz Quarada: {self.resOpe}')
          

calc1 = calculadoraSimples()
calc1.Iniciar()



""" op = input('Fazer outra operação? [S/N]: ').capitalize().strip()
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
                    print('Digite um valor inteiro!')"""