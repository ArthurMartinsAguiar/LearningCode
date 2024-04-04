'''O primeiro passo para implementar uma lista encadeada é criar uma
classe que a represente.'''

class LinkedList:
    def __init__(self):
        self.head = None

'''Próximo cria uma classe para representar os elementos que cada Node
da lista irá armazenar'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None  

