def floyd_warshall(grafo):
    dist = [[float('inf') for w in grafo] for n in grafo]
    pred = [[None for w in grafo] for n in grafo]
    indices = range(len(grafo))
    for i in indices:
        for j in indices:
            if i == j:
                dist[i][j] = 0
            elif grafo[i][j] != 0:
                dist[i][j] = grafo[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = float('inf')
                pred[i][j] = None

    for k in indices:
        for i in indices:
            for j in indices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return (dist, pred)