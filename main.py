# -*- coding: utf-8 -*-
from src.Candidate.Candidatos import Candidato
class Controle: 
    def __init__(self):
        self.__todosItens = []
        self.__dicionario = {}
        self.__printaBens = {}
        self.__printaDataNascimento = {}

        with open('./data/candidatosTotais.csv', 'r') as entrada:
            for linha in entrada:
                if 'DT_GERACAO' in linha:
                    continue
                linha = ((linha.replace('"','')).strip()).split(';')
                pessoa = Candidato(linha)
                self.getTodosItens().append()

        print(self.getTodosItens())

    
    def getTodosItens(self): return self.__todosItens
    def getDicionario(self): return self.__dicionario
    def getPrintaBens(self): return self.__printaBens
    def getPrintaDataNascimento(self): return self.__printaDataNascimento


    
if __name__ == '__main__':
    a = Controle()
    




