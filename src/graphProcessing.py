class Grafo:

    vertices=[]
    qntVertices=0
    indice=0
    marcado=[]
    numeroDeComponentes=0
    def __init__(self) -> None:
        pass

def Graph() -> Grafo:
    #criar novo grafo vazio
    grafo = Grafo()
    return grafo

def loadData(caminho,grafo) -> None:
    #preencher o grafo
    with open (caminho,"r") as arquivo:
        grafo.qntVertices = arquivo.readline()
        for i in range(0,int(grafo.qntVertices)+1):
            grafo.vertices.append([])
            grafo.marcado.append(False)
        for line in arquivo:
            linha = line.split()
            try:
                vert1 = int(linha[0])
                vert2 = int(linha[1])
                grafo.vertices[vert1].append(vert2)
                grafo.vertices[vert2].append(vert1)
            except:
                pass
        grafo.vertices.pop(0)


def minDegree(grafo) -> int:
    #grau minimo do grafo
    count = 0
    menorGrau = 999999999999999999999
    for i in range(0,len(grafo.vertices)):
        count=len(grafo.vertices[i])
        if count<menorGrau :
            menorGrau=count
    
    return menorGrau

def maxDegree(grafo) -> int:
    #grau maximo do grafo
    count = 0
    maiorGrau = 0
    novoGrafo.indice = 0
    for i in range(0,len(grafo.vertices)):
        count=len(grafo.vertices[i])
        if count>maiorGrau :
            maiorGrau=count
            novoGrafo.indice = i

    return maiorGrau

def numEdges(grafo) -> int:
    #numero de arestas do grafo
    count = 0
    for i in range(0,len(grafo.vertices)):
        count=count+len(grafo.vertices[i])
    return int(count/2)

def numVertex(grafo) -> int:
    #numero de vertices do grafo
    return len(grafo.vertices)

def components(grafo) -> int:
    #Busca em profundidade no grafo para retornar numero de componentes conexos
    grafo.numeroDeComponentes=0
    for i in range(0,len(grafo.vertices)):
        if(grafo.marcado[i]==False):
            BP(grafo,i)
            grafo.numeroDeComponentes+=1

    for i in range(0,len(grafo.marcado)):
        grafo.marcado[i]=False
    
    return grafo.numeroDeComponentes

def BP(grafo,verticeInicial) -> None:
    #BP Recursiva
    grafo.marcado[verticeInicial]=True
    for i in range(0,len(grafo.vertices[verticeInicial])):
        if(grafo.marcado[grafo.vertices[verticeInicial][i]-1]==False):
            BP(grafo,grafo.vertices[verticeInicial][i]-1)

def components_BP_Iterativa(grafo) -> int:
    #Busca em profundidade no grafo para retornar numero de componentes conexos
    grafo.numeroDeComponentes=0
    for i in range(0,len(grafo.vertices)):
        if(grafo.marcado[i]==False):
            BP_Iterativa(grafo,i)
            grafo.numeroDeComponentes+=1

    for i in range(0,len(grafo.marcado)):
        grafo.marcado[i]=False
    
    return grafo.numeroDeComponentes

def BP_Iterativa(graph, start_vertex) -> None:
    #Busca em profundidade iterativa
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if graph.marcado[vertex]==False:
            graph.marcado[vertex]=True
            # add vertex in the same order as visited:
            stack.extend(reversed(graph.vertices[vertex-1]))
    return

novoGrafo = Graph()

#loadData("<CAMINHO DO ARQUIVO>",novoGrafo)
loadData("C:/Users/JPC/Documents/ufs/[Semestres anteriores]/Grafos/dblp.txt",novoGrafo)

print("Grau minimo:",minDegree(novoGrafo))

print("Grau maximo:",maxDegree(novoGrafo),"- indice:",novoGrafo.indice,"- ID:",novoGrafo.indice+1)

print("Numero de arestas:",numEdges(novoGrafo))

print("Numero de vertices:",numVertex(novoGrafo))

#BP RECURSIVA RESULTA EM ESTOURO DO LIMITE DE RECURSÃO
#print("BP Recursiva - Num de componentes:",components(novoGrafo))

print("BP Iterativa - Num de componentes:",components_BP_Iterativa(novoGrafo))
