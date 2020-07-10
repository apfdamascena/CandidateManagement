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
        self.__valoresTotaisBens = 0
    
    def getAnoEleicao(self): return self.__anoEleicao
    def getSiglaEstado(self): return self.__siglaEstado
    def getCodigoCargo(self): return self.__codigoCargo
    def getDescricaoCargo(self): return self.__descricaoCargo
    def getNome(self): return self.__nome
    def getId(self): return self.__id
    def getNumeroUrna(self): return self.__numeroUrna
    def getCpf(self): return self.__cpf
    def getNomeUrna(self): return self.__nomeUrna
    def getNumeroPartido(self): return self.__numeroPartido
    def getNomePartido(self): return self.__nomePartido
    def getSiglaPartido(self): return self.__siglaPartido
    def getCodigoOcupacao(self): return self.__codigoOcupacao
    def getDescricaoOcupacao(self): return self.__descriOcupacao
    def getDataNascimento(self): return self.__dataNascimento
    def getSexo(self): return self.__sexo
    def getGrauInstrucao(self): return self.__grauInstrucao
    def getEstadoCivil(self): return self.__estadoCivil
    def getSiglaUfNascimento(self): return self.__siglaUFnascimento
    def getNomeMunicipioNascimento(self): return self.__nomeMunicipioNascimento
    def getSituacaoPosPleito(self): return self.__situacaoPosPleito
    def getSituacaoCandidatura(self): return self.__situacaoCandidatura

    def setAnoEleicao(self, ano): self.__anoEleicao = ano
    def setSiglaEstado(self, siglaEstado): self.__siglaEstado = siglaEstado
    def setCodigoCargo(self, codigoCargo): self.__codigoCargo = codigoCargo
    def setDescricaoCargo(self, descricaoCargo): self.__descricaoCargo = descricaoCargo 
    def setNome(self, nome): self.__nome = nome
    def setId(self, novaId): self.__id = novaId
    def setNumeroUrna(self, numeroUrna): self.__numeroUrna = numeroUrna
    def setCpf(self, cpf): self.__cpf = cpf
    def setNomeUrna(self, nomeUrna): self.__nomeUrna = nomeUrna
    def setNumeroPartido(self, numeroPartido): self.__numeroPartido = numeroPartido
    def setNomePartido(self, nomePartido): self.__nomePartido = nomePartido
    def setSiglaPartido(self, siglaPartido): self.__siglaPartido = siglaPartido
    def setCodigoOcupacao(self, codigoOcupacao): self.__codigoOcupacao = codigoOcupacao
    def setDescricaoOcupacao(self, descricaoOcupacao): self.__descriOcupacao = descricaoOcupacao
    def setDataNascimento(self, dataNascimento): self.__dataNascimento = dataNascimento
    def setSexo(self, sexo): self.__sexo = sexo
    def setGrauInstrucao(self, grauInstrucao): self.__grauInstrucao = grauInstrucao
    def setEstadoCivil(self, estadoCivil): self.__estadoCivil = estadoCivil
    def setSiglaUfNascimento(self, siglaUfNascimento): self.__siglaUFnascimento = siglaUfNascimento
    def setNomeMunicipioNascimento(self, nomeMunicipioNascimento): self.__nomeMunicipioNascimento = nomeMunicipioNascimento
    def setSituacaoPosPleito(self, situacaoPosPleito): self.__situacaoPosPleito = situacaoPosPleito
    def setSituacaoCandidatura(self, situacaoCandidatura): self.__situacaoCandidatura = situacaoCandidatura