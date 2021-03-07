class Grafo:

    def __init__(self, vertices):  #numero total de vertices do grafo
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] #matriz de adjacencias com 0 em todas posições

    #Função para adicionar arestas com peso, u e v são os vertices conectados
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        #trocar = por += se for grafo multiplas arestas
        #self.grafo[v-1][u-1] = 1 caso o gafo não seja direcionado

    def mostra_matriz(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

g = Grafo(4)

#g.adiciona_aresta(1,2, 5)
#g.adiciona_aresta(3,4, 9)
#g.adiciona_aresta(2,3, 3)
#g.mostra_matriz()

#Usuario informa a quantidade de vertices e os pesos dos vertices
v = int(input('Digite a quantidade de vértices: '))
g = Grafo(v)

a = int(input('Digite a quantidade de arestas: '))
for i in range(a):
    u = int(input('Vértice partida: '))
    v = int(input('Vértice chegada: '))
    p = int(input('Peso da aresta:'))
    g.adiciona_aresta(u, v, p)

g.mostra_matriz()

