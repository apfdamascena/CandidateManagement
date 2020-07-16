# -*- coding: utf-8 -*-
from src.Candidato.Candidatos import Candidato
from src.Bens.Bem import Bem

class Controle: 
    def __init__(self):
        self.__todosItens = []
        self.__dicionario = {}
        self.__printaBens = {}
        self.__printaDataNascimento = {}

        with open('./data/candidatosTotais.csv', 'r', encoding="ISO-8859-1") as entrada:
            cont = 0
            for linha in entrada:
                if(cont == 1000): break
                cont += 1
                if 'DT_GERACAO' in linha: continue
                linha = ((linha.replace('"','')).strip()).split(';')
                pessoa = Candidato(linha)
                self.getTodosItens().append(pessoa)

        with open('./data/bemCandidatos.csv', 'r', encoding="ISO-8859-1") as entrada:
            for linha in entrada:
                if 'DT_GERACAO' in linha: continue
                linha = ((linha.replace('"','')).strip()).split(';')
                bens = Bem(linha)
                currentId = bens.getId()
                if currentId not in self.getDicionario():
                    self.getDicionario()[currentId] = []
                    self.getDicionario()[currentId].append(bens)
                else: self.getDicionario()[currentId].append(bens)
            self.incluindoBens()
        print(self.getTodosItens())
        
    def getTodosItens(self): return self.__todosItens
    def getDicionario(self): return self.__dicionario
    def getPrintaBens(self): return self.__printaBens
    def getPrintaDataNascimento(self): return self.__printaDataNascimento

    def incluindoBens(self):
        for itens in self.getTodosItens():
            currentId = itens.getId()
            if currentId in self.getDicionario():
                for bens in self.getDicionario()[currentId]:
                    itens.incluirBem(bens)
            else: continue

    def apresentaNomeEmOrdemCrescente(self):
        sortedInfo = sorted(self.getTodosItens(), key=lambda candidato: candidato.getNome())
        for infos in sortedInfo: print(infos)
    
if __name__ == '__main__':
    a = Controle()
    a.apresentaNomeEmOrdemCrescente()