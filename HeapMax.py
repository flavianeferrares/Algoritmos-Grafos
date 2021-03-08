import math

class HeapMax:

    def __init__(self):
        self.nos = 0  #quantidade de nos
        self.heap = []

    def adiciona_no(self, u):  #u valor do no, adiciona na ultima posição
        self.heap.append(u)
        self.nos += 1
        f = self.nos  #f = filho
        while True:
            if f == 1:
                break
            p = f // 2  #p = pai, // faz a divisão inteira
            if self.heap[p-1] >= self.heap[f-1]: # <= HeapMin
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
                if self.heap[f] > self.heap[f-1]: # < se for HeapMin
                    f += 1

            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1]
                p = f

        return x

    def tamanho(self):
        return self.nos

    def maiorElemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'Arvore vazia'

    def filho_esquerda(self, i):
        if self.nos >= 2 * i:
            return self.heap[2 * i - 1]
        return 'Não a filhos a esquerda!'

    def filho_direita(self, i):
        if self.nos >= 2 * i + 1:
            return self.heap[2 * i]
        return 'Não a filhos a direita!'

    def pai(self, i):
        return self.heap[i // 2]





h = HeapMax()

h.adiciona_no(17)
h.adiciona_no(36)
h.adiciona_no(25)
h.adiciona_no(7)
h.adiciona_no(3)
h.adiciona_no(100)
h.adiciona_no(1)
h.adiciona_no(2)
h.adiciona_no(19)

elementoMax = h.remove_no()
print('Elemento retirado: ', elementoMax)

h.mostra_heap()

print(f'Tamanho: {h.tamanho()}')

print(f'Filho esquerda de 17: {h.filho_esquerda(4)}')
print(f'Filho a direita 17: {h.filho_direita(4)}')

