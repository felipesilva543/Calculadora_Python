from icecream import ic
def menu(titulo=0, *msg):
    """
    -> Função para criar um escopo de menu
    param msg: lista de itens no menu, O primeiro deve ser o titúlo do menu
    param titulo: Se titulo = 0 vai mostrar o título, caso titulo = 1 não vai mostrar
    return: A quantidade de itens do menu
    """
    tam = len(msg[0])
    for i in msg:
        if tam < len(i):
            tam = len(i)

    tam += 4

    if titulo == 0:
        print('\033[34m-'*(tam))
        print(f'{msg[0]}'.center(tam))
        print('\033[34m-'*(tam),'\033[m')
        for i in range(1, len(msg)):
            print(f'\033[32m{i}\033[m - \033[34m{msg[i]}\033[m')
        if len(msg) > 1:
            print('\033[34m-\033[m'*(tam))
        return len(msg) -1
    else:
        print('\033[34m-'*(tam),'\033[m')
        for i in range(0, len(msg)):
            print(f'\033[32m{i+1}\033[m - \033[34m{msg[i]}\033[m')
        if len(msg) > 1:
            print('\033[34m-\033[m'*(tam))
        return len(msg) -1
    