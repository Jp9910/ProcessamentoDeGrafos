import sys
class Grafo:

    vertices=[]
    qntVertices=0
    indice=0
    marcado=[]
    numeroDeComponentes=0
    def __init__(self) -> None:
        pass

#Implementar como funcões da classe ou como funções separadas??
#Como transformar em uma biblioteca?
#'v.comp := ncomp' no slide 38 de BP?
#Limite de recursão na funçao BP?

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
            vert1 = int(linha[0])
            vert2 = int(linha[1])
            grafo.vertices[vert1].append(vert2)
            grafo.vertices[vert2].append(vert1)
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

    return grafo.numeroDeComponentes

def BP(grafo,verticeInicial) -> None:
    grafo.marcado[verticeInicial]=True
    for i in range(0,len(grafo.vertices[verticeInicial])):
        if(grafo.marcado[grafo.vertices[verticeInicial][i]-1]==False):
            BP(grafo,grafo.vertices[verticeInicial][i]-1)

novoGrafo = Graph()

loadData("C:/Users/JPC/Documents/ufs/Grafos/dblp.txt",novoGrafo)

print("Grau minimo:",minDegree(novoGrafo))

print("Grau maximo:",maxDegree(novoGrafo),"- indice:",novoGrafo.indice)

print("Numero de arestas:",numEdges(novoGrafo))

print("Numero de vertices:",numVertex(novoGrafo))

#sys.setrecursionlimit(4000)

print("Numero de componentes:", components(novoGrafo))

#print(novoGrafo.vertices)
#print(novoGrafo.marcado[novoGrafo.vertices[0][0]])
#print(novoGrafo.vertices[0][0])

#print(novoGrafo.vertices[0])
#print(novoGrafo.vertices[18])
#print(novoGrafo.vertices[502443])
