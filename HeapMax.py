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

h.mostra_heap()