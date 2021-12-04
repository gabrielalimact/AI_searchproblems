# considerando os estados em forma de vetor:
# [0] -> missionários do lado esquerdo
# [1] -> canibais do lado esquerdo
# [2] -> missionários do lado direito
# [3] -> canibais do lado direito
# [4] -> posição da canoa (0 = esquerda, 1 = direita)
# por isso, o estado inicial é: [3,3,0,0,0]
firstState = [3, 3, 0, 0, 0]

# os operadores são as ações que podem ser tomadas a partir do estado inicial:
# (1,0) - atravessar um missionario no barco
# (2,0) - atravessar dois missionarios no barco
# (1,1) - atravessar 1 canibal e 1 missionario
# (0,2) - atravessar dois canibais
# (0,1) - atravessar um canibal - inválida
# porém, se pararmos para analisar a ação de atravessar somente um canibal, não conseguimos ver uma forma de chegar a solução final.
operators = [(1, 0), (2, 0), (1, 1), (0, 2)]

edgeList = []
visited = []


# função que move o barco de uma margem para outra, nm -> número de missionários, nc -> número de canibais
def moveBoat(fState, nm=0, nc=0):
    if nm+nc > 2:  # não podemos transportar mais que 2 pessoas
        return

    # verificando em qual lado está a canoa e alocando a posição (origem e destino) dos missionários e canibais no array
    if fState[-1] == 0:
        mo = 0
        co = 1
        md = 2
        cd = 3
    else:
        mo = 2
        co = 3
        md = 0
        cd = 1

    # se não houver missionários nem canibais no barco, não podemos atravessar
    if fState[mo] == 0 and fState[co] == 0:
        return

    for i in range(min(nm, fState[mo])):  # atualiza a posição dos missionários
        fState[mo] -= 1
        fState[md] += 1

    for i in range(min(nc, fState[co])):  # atualiza a posição dos canibais
        fState[co] -= 1
        fState[cd] += 1

    fState[-1] = 1-fState[-1]  # atualizando a posição da canoa

    return fState


# função para calcular os próximos estados válidos a partir do estado atual
def sucessors(state):
    sucessors = []

    for (i, j) in operators:
        s = moveBoat(state[:], i, j)

        if s == None:
            continue
        if s in visited:  # se o estado já foi visitado, não adicionamos
            continue
        # verificar se a qntd de missionários é menor q a de canibais
        if (s[0] < s[1] and s[0] > 0) or (s[2] < s[3] and s[2] > 0) or ():
            continue

        # se não, adicionamos o estado ao conjunto de sucessores
        sucessors.append(s)
    return sucessors


def testSuccess(state):  # verifica se o estado é o estado final, CONDIÇÃO DE PARADA da busca
    if state[2] >= 3 and state[3] >= 3:
        return True
    else:
        return False


def notVisited(element):  # busca em profundidade precisa que o no não esteja na lista de visitados
    l = sucessors(element)
    if len(l) > 0:
        return l[0]  # retorna o primeiro elemento de sucessors
    else:
        return -1


def searching(firstState):  # buscando em profundidade
    edgeList.append(firstState)

    while len(edgeList) != 0:
        element = edgeList[len(edgeList)-1]

        if testSuccess(element):  # condição de parada: verifica se é o estado final
            break

        v = notVisited(element)
        if v == -1:
            edgeList.pop()
        else:
            visited.append(v)
            edgeList.append(v)
    else:
        print("ERROR! Not found.")

    return edgeList


solution = searching(firstState)


for i in range(1, len(solution)):  # imprimindo a solução junto com as ações
    md = abs(solution[i][0]-solution[i-1][0])
    cd = abs(solution[i][1]-solution[i-1][1])
    boat = solution[i][4] - solution[i-1][4]

    if boat == 1:
        s = "direita ->"
    else:
        s = "esquerda <-"
    print(
        "\nestado atual: ", solution[i-1], "\nmover ({} missionários, {} canibais para a {})".format(md, cd, s))
print("")
print(solution[-1], " é o estado final.")
