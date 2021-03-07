class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]  #Lista de adjacencias

    def adiciona_aresta(self, u, v):
        #Grafos direcionado sem peso nas arestas
        self.grafo[u-1].append(v-1)

        #self.grafo[v-1].append(u) se o grafo não direcionado

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f'{j+1} ->', end=' ')
            print('')
g = Grafo(4)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(1, 3)
g.adiciona_aresta(1, 4)
g.adiciona_aresta(2, 3)

g.mostra_lista()

