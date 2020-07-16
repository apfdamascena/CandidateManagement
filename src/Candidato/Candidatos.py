class Candidato:
    def __init__(self, iteravel):
        self.__anoEleicao = iteravel[2]
        self.__siglaEstado = iteravel[10]
        self.__codigoCargo = iteravel[13]
        self.__descricaoCargo = iteravel[14]
        self.__nome = iteravel[17]
        self.__id = iteravel[15]
        self.__numeroUrna = iteravel[16]
        self.__cpf = iteravel[21]
        self.__nomeUrna = iteravel[18]
        self.__numeroPartido = iteravel[27]
        self.__nomePartido = iteravel[29]
        self.__siglaPartido = iteravel[28]
        self.__codigoOcupacao = iteravel[49]
        self.__descriOcupacao = iteravel[50]
        self.__dataNascimento = iteravel[38]
        self.__sexo = iteravel[42]
        self.__grauInstrucao = iteravel[44]
        self.__estadoCivil = iteravel[46]
        self.__siglaUFnascimento = iteravel[35]
        self.__nomeMunicipioNascimento = iteravel[37]
        self.__situacaoPosPleito = iteravel[53]
        self.__situacaoCandidatura = iteravel[25]
        self.__bens = []
        self.valoresTotaisBens = 0
    
    def getSiglaEstado(self): return self.__siglaEstado
    def getCodigoCargo(self): return self.__codigoCargo
    def getDescricaoCargo(self): return self.__descricaoCargo
    def getNome(self): return self.__nome
    def getId(self): return self.__id
    def getNumeroUrna(self): return self.__numeroUrna
    def getNomeUrna(self): return self.__nomeUrna
    def getSiglaPartido(self): return self.__siglaPartido
    def getDescricaoOcupacao(self): return self.__descriOcupacao
    def getSiglaUfNascimento(self): return self.__siglaUFnascimento
    def getNomeMunicipioNascimento(self): return self.__nomeMunicipioNascimento
    def getBens(self): return self.__bens
    def getValoresTotaisBens(self): return self.valoresTotaisBens

    def incluirBem(self,objeto):
        todosItens = objeto.getInfoList()
        valorAdiciona = float(todosItens[3].replace(',','.'))
        self.getBens().append(todosItens)
        self.valoresTotaisBens += valorAdiciona
    
    def transformaListaEmDicionario(self):
        dicionario = {}
        for bens in self.getBens():
            item = int(bens[0])
            if(item not in dicionario):
                dicionario[item] = bens[2:]
            else: dicionario[item] += bens[3:4]
        return dicionario
    
    def apresentaDicionario(self,dicionario):
        apresentacao = ''
        valor = 0
        for bens in dicionario:
            apresentacao += dicionario[bens][0]
            for conteudo in dicionario[bens][1:]:
                currentValor = float(conteudo.replace(',','.'))
                valor += currentValor
            apresentacao += ' |---> ' + str(valor) + '\n' + '     '
        return apresentacao

    def apresentaBensDatalhados(self):
        apresentacao = ''
        informacao = self.getBens()
        for bensIndex in range(len(informacao)):
            apresentacao += informacao[bensIndex][1] + ' |---> ' + 'R$ ' + informacao[bensIndex][3] + '\n' + '       ' + ' '
        return "Bens detalhados: " + "\n" + "        " + apresentacao

    def __str__(self):
        return '\n' + self.getNomeUrna() + ' -- ' + self.getNumeroUrna() + ' -- '+ self.getSiglaPartido()+'\n' + self.getDescricaoCargo()+' (' + self.getSiglaEstado() + ') ' + self.getNomeMunicipioNascimento()+ ' (' + self.getSiglaUfNascimento() + ') ' + '\n' + 'NOME: ' + self.getNome() +'\n' + 'RESUMO DOS BENS: ' + '\n' + '\n' + '    -' + 'TOTAL DECLARADO: ' + 'R$ ' + str(self.getValoresTotaisBens()) + '\n' + '    -' + 'TOTAL POR TIPO DE BEM: ' + self.apresentaDicionario(self.transformaListaEmDicionario())

    def __repr__(self): return "DadosSobreCandidato(" + self.__str__() + ")"