import math

class HeapMin:

    def __init__(self):
        self.nos = 0  #quantidade de nos
        self.heap = []

    def adiciona_no(self, u, indice):  # u sera o peso
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos  #f = filho
        while True:
            if f == 1:
                break
            p = f // 2  #p = pai, // faz a divisão inteira
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        #print(self.heap) forma de impressão simples
        print('A estrutura heap é a seguinte: ')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end=' ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end=' ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos: #filho a esquerda
                break
            if f+1 <= self.nos:  #filho a direita
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1

            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1]
                p = f

        return x

    def tamanho(self):
        return self.nos


class Grafo:  #Nao_Direcionado

    def __init__(self, vertices):  #numero total de vertices do grafo
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] #matriz de adjacencias com 0 em todas posições

    #Função para adicionar arestas com peso , u e v são os vertices conectados
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkastra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)] #custo_vem_De_qual_vertice, -1 para o algoritmo e infinito.
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):  #percorre a linha dos vertices na matriz de distancias
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem

g = Grafo(7)
g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(1, 3, 6)
g.adiciona_aresta(1, 4, 10)
g.adiciona_aresta(2, 5, 13)
g.adiciona_aresta(3, 4, 3)
g.adiciona_aresta(3, 5, 11)
g.adiciona_aresta(3, 6, 6)
g.adiciona_aresta(4, 5, 6)
g.adiciona_aresta(4, 6, 4)
g.adiciona_aresta(5, 7, 3)
g.adiciona_aresta(6, 7, 8)

g.mostra_matriz()

resultado_dijktra = g.dijkastra(1)
print(resultado_dijktra)