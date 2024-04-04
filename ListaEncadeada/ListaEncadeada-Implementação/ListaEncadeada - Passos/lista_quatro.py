class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    
    def __init__(self, nodes = None) -> None:
        self.head = None
        if nodes is not None: # Essa linha verifica se houve algum argumento passado
            node = Node(data = nodes.pop(0)) #Cria um node a partir do primeiro elemento do argumento passado à cabeça da lista.
            self.head = node #Define o node criado como inicio da lista
            for elem in nodes:#loop apartir de todos os elementos do argumento passado
                node.next = Node(data = elem)#cria um novo node que passa a ser o próximo node do anterior
                node = node.next#define como o node atual

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_end(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

'''Inserindo no inicio da lista'''
llist = LinkedList()
print(llist)

llist.add_first(Node("b"))
print(llist)

llist.add_first(Node("a"))
print(llist)
''''''

'''Inserindo no final da lista'''
llist_end = LinkedList(["a", "b", "c", "d"])
print(llist_end)

llist_end.add_end(Node("e"))
print(llist_end)

llist_end.add_end(Node("f"))
print(llist_end)

''''''