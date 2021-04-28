from queue import PriorityQueue
from typing import List, Tuple


def djikstra(grafo, s):

    dist = [float('inf') for v in grafo]
    pred = [None for v in grafo]
    dist[s] = 0
    Q: PriorityQueue = PriorityQueue()
    Q.put((0, s))
    elementos = 1

    while elementos != 0:
        elemento: Tuple[int, float] = Q.get()
        elementos -= 1
        distancia: float = elemento[0]
        atual: int = elemento[1]
        if distancia > dist[atual]:
            continue
        adjacentes: List[Tuple[int, float]] = [(c, n) for c, n in enumerate(grafo[atual]) if n != 0]
        for v, w in adjacentes:
            if dist[v] > dist[atual] + w:
                dist[v] = dist[atual] + w
                pred[v] = atual
                Q.put((w, v))
                elementos += 1

    return (dist, pred)
