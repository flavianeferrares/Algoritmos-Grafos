def bellman_ford(grafo, s):
    dist = [float('inf') for v in grafo]
    pred = [None for v in grafo]
    dist[s] = 0
    arestas = []
    indices = range(len(grafo))

    for i in indices:
        for j in indices:
            if grafo[i][j] != 0:
                arestas.append((i, j))

    for l in indices:
        for aresta in arestas:
            u, v = aresta
            if dist[v] > dist[u] + grafo[u][v]:
                dist[v] = dist[u] + grafo[u][v]
                pred[v] = u

    return (dist, pred)