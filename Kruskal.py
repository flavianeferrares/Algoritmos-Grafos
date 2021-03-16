pai = dict() #dict() cria um dicionario
classificacao = dict()


def make_set(v): #cria conjunto
    pai[v] = v
    classificacao[v] = 0


def find(v): #encontra conjunto
    if pai[v] != v:
        pai[v] = find(pai[v])
    return pai[v]


def union(v1, v2):
    raiz1 = find(v1)
    raiz2 = find(v2)
    if raiz1 != raiz2:
        if classificacao[raiz1] > classificacao[raiz2]:
            pai[raiz2] = raiz1
        else:
            pai[raiz1] = raiz2
        if classificacao[raiz1] == classificacao[raiz2]: classificacao[raiz2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice) #cria uma 'floresta' conjunto para cada vertice
        arvore_geradora_min = set() #set e uma collection que representa conjunto onde não existe repetição de elementos
        arestas = list(graph['arestas'])
        arestas.sort() #ordena as arestas por peso

    for aresta in arestas:
        w, u, v = aresta
        if find(u) != find(v): #vertice origem != de vertice destino não forma ciclo
            union(u, v)
            arvore_geradora_min.add(aresta)

    return sorted(arvore_geradora_min)


graph = {
    'vertices': ['0', '1', '2', '3', '4', '5', '6', '7'],
    'arestas': set([
        (1, '1', '2'),
        (1, '1', '7'),
        (1, '2', '3'),
        (1, '4', '5'),
        (2, '0', '1'),
        (2, '3', '5'),
        (3, '0', '7'),
        (3, '2', '5'),
        (4, '3', '4'),
        (4, '6', '7'),
        (5, '2', '6'),
        (6, '5', '6'),
        (7, '1', '6')
    ])
}

print(kruskal(graph))