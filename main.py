#Vars
alfabeto = ["-"]
estadoAceitacao = []
transicoes = {}
testes = []

##Leitura Entrada##
def LerEntrada():
    entrada = open("entrada.txt", "r")

    #Alfabeto
    linhaAlfabeto = entrada.readline()
    linhaAlfabeto = linhaAlfabeto.replace("\n", "")
    for letra in linhaAlfabeto:
        alfabeto.append(letra)

    #Estados
    linhaestadoAceitacao = entrada.readline()
    linhaestadoAceitacao = linhaestadoAceitacao.replace("\n", "")
    estadoAceitacao.append(linhaestadoAceitacao)

    #Transições
    qtdTransicoes = entrada.readline()

    for _ in range(int(qtdTransicoes)):
        linhaTransicao = entrada.readline()
        linhaTransicao = linhaTransicao.replace("\n", "")

        estadoCorrente, simbolo, escrita, direcao, novoEstado = linhaTransicao.split(" ")
        transicoes[f"{estadoCorrente},{simbolo}"] = [escrita, direcao, novoEstado]

    #Testes
    qtdTestes = entrada.readline()

    for _ in range(int(qtdTestes)):
        linhaTeste = entrada.readline()
        linhaTeste = linhaTeste.replace("\n", "")
        testes.append(linhaTeste)

    entrada.close()

##Simulação##
def Simular(fitaEntrada):
    #A sequência de entrada está na pos 1 da fita para que exista um - na pos 0
    #Dessa forma fica fácil de fazer a agulha voltar para o início da fita sem estourar o limite do vetor 
    fita = "-" + fitaEntrada + "-" * (99 - len(fitaEntrada))
    estadoAtual = 1
    posAgulha = 1

    #Enquanto n chegar no estado final
    while estadoAtual != estadoAceitacao[0]:
        # print(fita, estadoAtual, f"({posAgulha},{fita[posAgulha]})")
        chave = f"{estadoAtual},{fita[posAgulha]}"

        #Olha se existe uma transição para o par estado Atual e valor lido na fita
        #Caso não exista transição vai para o estado de rejeição e para a execução
        if chave in transicoes:
            transicao = transicoes[chave]
        else:        
            return "not OK"

        #Realizar transição
        fitaList = list(fita)
        fitaList[posAgulha] = transicao[0]
        fita = "".join(fitaList)

        posAgulha = (posAgulha+1) if transicao[1] == 'D' else (posAgulha-1)
        estadoAtual = transicao[2]
    return "OK"

##Main##
LerEntrada()

for idx, teste in enumerate(testes):
    resultado = Simular(teste)
    print(f"{idx+1}: {teste} {resultado}")
