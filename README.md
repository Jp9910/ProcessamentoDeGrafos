# ProcessamentoDeGrafos
Biblioteca em python para criar e processar dados na forma de grafos não direcionados.

## Formato do grafo

#### Vértices
"vertices" é um vetor de duas dimensões que representará os vértices do grafo e suas conexões.
A primeira dimensão representa cada vértice. A segunda dimensão representa os vértices que estão conexos ao vértice da primeira dimensão.
Ex:
vertices[544] é um vetor que conterá todas as conexões do vértice de número 544.
vertice[544][0] é a primeira conexão do vértice 544, se existir.
vertice[544][2] é a terceira conexão do vértice 544, se existir.

#### Quantidade de vértices
"qntVertices" É a quantidade de vértices do grafo. É simplesmente a primeira linha do arquivo de dados.

#### Maior grau
"indice" é o índice do vertice que tem o maior grau (maior quantidade de arestas).

#### Marcações
"marcado" é um vetor que indicará se o vértice já foi marcado ou não
Ex:
se marcado[544] for = false, o vertice[544] ainda não foi marcado
se marcado[544] for = true, o vertice[544] já foi marcado

#### Componentes
"numeroDeComponentes" representa o número de componentes conexos que existe no grafo

## Input format
Quantidade de vértices, seguido das arestas (2 vértices).

> Quantidade de vértices

> VérticeA VérticeB

Ex:
>544

>1 344

>1 130

>1 500

>2 433

>5 69

>9 82

>3 234

>532 95

>...