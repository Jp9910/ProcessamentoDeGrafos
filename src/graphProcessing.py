class Grafo:

    vertices=[]
    qntVertices=0
    indice=0
    def __init__(self) -> None:
        pass

#Implementar como funcões da classe ou como funções separadas??
#Como transformar em uma biblioteca?

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
        for line in arquivo:
            linha = line.split()
            vert1 = int(linha[0])
            vert2 = int(linha[1])
            grafo.vertices[vert1].append(vert2)
            grafo.vertices[vert2].append(vert1)
        grafo.vertices.pop(0)


def minDegree(grafo) -> int:
    #grau minimo do grafo
    count = 0
    menorGrau = 999999999999999999999
    print(menorGrau,type(menorGrau))
    for i in range(0,len(grafo.vertices)):
        count=0
        for j in range(0,len(grafo.vertices[i])):
            count=count+1
        if count<menorGrau :
            menorGrau=count
    
    return menorGrau

def maxDegree(grafo) -> int:
    #grau maximo do grafo
    count = 0
    maiorGrau = 0
    novoGrafo.indice = 0
    for i in range(0,len(grafo.vertices)):
        count=0
        for j in range(0,len(grafo.vertices[i])):
            count=count+1
        if count>maiorGrau :
            maiorGrau=count
            novoGrafo.indice = i

    return maiorGrau

def numEdges(grafo) -> int:
    #numero de arestas do grafo
    count = 0
    for i in range(0,len(grafo.vertices)):
        for j in range(0,len(grafo.vertices[i])):
            count=count+1
    return int(count/2)

def numVertex(grafo) -> int:
    #numero de vertices do grafo
    return len(grafo.vertices)

def components() -> None:
    #Busca em profundidade no grafo para retornar numero de componentes conexos
    pass

novoGrafo = Graph()

loadData("C:/Users/JPC/Documents/ufs/Grafos/dblp.txt",novoGrafo)

print("Grau minimo:",minDegree(novoGrafo))

print("Grau maximo:",maxDegree(novoGrafo),"- indice:",novoGrafo.indice)

print("Numero de arestas:",numEdges(novoGrafo))

print("Numero de vertices:",numVertex(novoGrafo))


print(novoGrafo.vertices[18])
print(novoGrafo.vertices[502443])
print(novoGrafo.vertices[novoGrafo.indice-1])
#print(novoGrafo.vertices[novoGrafo.indice])
print(novoGrafo.vertices[novoGrafo.indice+1])
