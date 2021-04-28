from itertools import permutations
from typing import List

from util import getCost


def forca_bruta(grafo) -> List[int]:
    tam = len(grafo)
    minCost = float('inf')
    bestPath = None

    for p in permutations(range(tam)):
        path: List[int] = list(p)
        path.append(path[0])
        cost = getCost(grafo, path)
        if minCost > cost:
            minCost = cost
            bestPath = path

    return bestPath