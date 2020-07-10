class Controle: 
    def __init__(self):
        self.__todosItens = []
        self.__dicionario = {}
        self.__printaBens = {}
        self.__printaDataNascimento = {}

        with open('./data/candidatosTotais.csv') as entrada:
            cont = 0
            for linha in entrada:
                cont += 1
                if( cont == 3): break
                if('DT_GERACAO' in linha):
                    continue
                linha = ((linha.replace('"','')).strip()).split(';')
                self.getTodosItens().append()
        print(self.getTodosItens())

    
    def getTodosItens(self): return self.__todosItens
    def getDicionario(self): return self.__dicionario
    def getPrintaBens(self): return self.__printaBens
    def getPrintaDataNascimento(self): return self.__printaDataNascimento


    

    




