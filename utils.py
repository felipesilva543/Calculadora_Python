from icecream import ic
def menu(txt = 'Exemplo'):
    """
    param txt: Texto para montar um menu
    """
    tamTxt = len(txt) + 4

    print('-'*tamTxt)
    print(f'{txt}'.center(tamTxt))
    print('-'*tamTxt)
