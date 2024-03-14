from collections import deque

'''
Queues implementation is based on FIFO algorithm.
This struct tells that the first element insert is also the first to go out.
'''

def createQueue() -> deque: #cria uma fila/queue vazia.  
    return deque()

def insertQueue(queue: deque, value):#insere valores dentro da fila criada, insere no final.
    queue.append(value)

def removeFromQueue(queue: deque):#retira o primeiro elemento da fila/queue.
    queue.popleft()

positions = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
fila = createQueue()
for p in positions:
    insertQueue(fila, p)

print(f"Fila completa {fila}")
print("\nRemovendo o primeiro elemento da fila: ") 
for remove in range(len(fila)): #Remove o primeiro elemento da fila até que fique vazia.
    removeFromQueue(fila)
    print(fila)
        

