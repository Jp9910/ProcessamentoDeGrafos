class Grafo:
    def __init__(self) -> None:
        self.vertices=[]
        self.qntVertices=0
        self.indice=0
        self.marcado=[]
        self.numeroDeComponentes=0

def newGraph() -> Grafo:
    """Retorna um novo grafo vazio"""
    grafo = Grafo()
    return grafo

def loadData(caminho,grafo) -> None:
    """preenche o grafo"""
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
    """retorna o grau minimo do grafo"""
    count = 0
    menorGrau = 999999999999999999999
    for i in range(0,len(grafo.vertices)):
        count=len(grafo.vertices[i])
        if count<menorGrau :
            menorGrau=count
    
    return menorGrau

def maxDegree(grafo) -> int:
    """retorna o grau maximo do grafo"""
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
    """retorna numero de arestas do grafo"""
    count = 0
    for i in range(0,len(grafo.vertices)):
        count=count+len(grafo.vertices[i])
    return int(count/2)

def numVertex(grafo) -> int:
    """retorna o numero de vertices do grafo"""
    return len(grafo.vertices)

def components(grafo) -> int:
    """
    Busca em profundidade recursiva no grafo para retornar numero de componentes conexos
    
    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
    
    - Auxiliary Space: O(V), since an extra visited array of size V is required.
    """
    grafo.numeroDeComponentes=0
    for i in range(0,len(grafo.vertices)):
        # Vai começar com o primeiro vértice sempre desmarcado. Os próximos só estarão desmarcados se não fizerem parte do grafo conexo do vértice inicial.
        if(grafo.marcado[i]==False):
            # Aqui ele marcará TODOS os vértices que possuem conexão (direta ou não) com o primeiro, ou seja todo o grafo conexo a partir do vértice inicial.
            BP(grafo,i)
            # Ou seja, se achou algum vértice desmarcado depois de executar BP, adiciona mais um grafo conexo.
            grafo.numeroDeComponentes+=1

    for i in range(0,len(grafo.marcado)):
        # Desmarcar todos os vértices após a busca.
        grafo.marcado[i]=False
    
    return grafo.numeroDeComponentes

def BP(grafo,verticeInicial) -> None:
    """Busca em profundidade recursiva"""
    grafo.marcado[verticeInicial]=True #Buscar a partir do vértice inicial. Considerá-lo então como marcado
    for i in range(0,len(grafo.vertices[verticeInicial])): #Pra cada aresta desse vértice inicial
        if(grafo.marcado[grafo.vertices[verticeInicial][i]-1]==False): #Se o vértice da outra ponta da aresta ainda não foi marcado
            BP(grafo,grafo.vertices[verticeInicial][i]-1) #Executar BP nesse vértice da outra ponta

def components_BP_Iterativa(grafo) -> int:
    """Busca em profundidade iterativa no grafo para retornar numero de componentes conexos"""
    grafo.numeroDeComponentes=0
    for i in range(0,len(grafo.vertices)):
        if(grafo.marcado[i]==False):
            BP_Iterativa(grafo,i)
            grafo.numeroDeComponentes+=1

    for i in range(0,len(grafo.marcado)):
        grafo.marcado[i]=False
    
    return grafo.numeroDeComponentes

def BP_Iterativa(graph, start_vertex) -> None:
    """Busca em profundidade iterativa"""
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if graph.marcado[vertex]==False:
            graph.marcado[vertex]=True
            # add vertex in the same order as visited:
            stack.extend(reversed(graph.vertices[vertex-1]))
    return

novoGrafo = Grafo()

#loadData("<CAMINHO DO ARQUIVO>",novoGrafo)
loadData("C:/Users/JPC/Documents/ufs/[Semestres anteriores]/Grafos/dblp.txt",novoGrafo)

print("Grau minimo:",minDegree(novoGrafo))

print("Grau maximo:",maxDegree(novoGrafo),"- indice:",novoGrafo.indice,"- ID:",novoGrafo.indice+1)

print("Numero de arestas:",numEdges(novoGrafo))

print("Numero de vertices:",numVertex(novoGrafo))

#BP RECURSIVA RESULTA EM ESTOURO DO LIMITE DE RECURSÃO
#print("BP Recursiva - Num de componentes:",components(novoGrafo))

print("BP Iterativa - Num de componentes:",components_BP_Iterativa(novoGrafo))
