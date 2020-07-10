import textwrap

class Bem:
    def __init__(self,iteravel):
        self.__codigoTipoBem = iteravel[13]
        self.__descricaoTipoBem = iteravel[14]
        self.__descricaoDetalhadaBem = iteravel[15]
        self.__valorBem = iteravel[16]
        self.__id = iteravel[11]
    
    def getCodigoTipoBem(self): return self.__codigoTipoBem
    def getDescricaoTipoBem(self): return self.__descricaoTipoBem
    def getDescricaoDetalhadaBem(self): return self.__descricaoDetalhadaBem
    def getValorBem(self): return self.__valorBem
    def getId(self): return self.__id

    def setCodigoTipoBem(self, codigoTipoBem): self.__codigoTipoBem = codigoTipoBem
    def setDescricaoTipoBem(self, descricaoTipoBem): self.__descricaoTipoBem = descricaoTipoBem
    def setDescricaoDetalhadaBem(self, descricaoDetalhadaBem): self.__descricaoDetalhadaBem = descricaoDetalhadaBem
    def setId(self, novaId): self.__id = novaId
    def setValorBem(self, valor):
        valor = float(valor.replace(',','.'))
        self.__valorBem = valor
    
    def adicionaValorBem(self,valor):
        valor = float(valor.replace(",","."))
        self.__valorBem += valor
    
    def getInfoList(self):
        return [self.getCodigoTipoBem(),self.getDescricaoDetalhadaBem(),self.getDescricaoTipoBem(),self.getValorBem()]