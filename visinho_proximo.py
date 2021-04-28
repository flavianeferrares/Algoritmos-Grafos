from typing import List

def vizinho_proximo(grafo) -> List[int]:
    u = 0
    C: List[int] = [u]
    tam = len(grafo)
    Q: List[int] = []
    v = None

    for i in range(tam):
        Q.append(i)
    Q.remove(u)

    while (Q != 0):
        menor = float('inf')
        continua = False
        for i in range(tam):
            if grafo[u][i] != 0 and grafo[u][i] < menor and Q.count(i) != 0:
                menor = grafo[u][i]
                v = i
                continua = True

        if continua:
                C.append(v)
                Q.remove(v)
                u = v

        else:
            break

    C.append(C[0])
    return C