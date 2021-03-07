class Grafo:

    def __init__(self, vertices):  #numero total de vertices do grafo
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] #matriz de adjacencias com 0 em todas posições

    #Função para adicionar arestas, u e v são os vertices conectados
    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        #trocar = por += se for grafo multiplas arestas
        #self.grafo[v-1][u-1] = 1 caso o gafo não seja direcionado

    def mostra_matriz(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

g = Grafo(4)
g.adiciona_aresta(1,2)
g.adiciona_aresta(3,4)
g.adiciona_aresta(2,3)
g.mostra_matriz()