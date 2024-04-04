'''Ao definir um node valores data e next permite que voce crie listas encadeadas de forma rápida.
A classe LinkedList e Node são os pontos de inicio para nossa implementação, a partir de agora
é tudo melhorar suas funcionalidades'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    '''Uma pequena mudança no __init__() permite que vc crie rapidamente listas encadeadas com alguns dados'''
    def __init__(self, nodes = None) -> None:
        self.head = None
        if nodes is not None: # Essa linha verifica se houve algum argumento passado
            node = Node(data = nodes.pop(0)) #Cria um node a partir do primeiro elemento do argumento passado à cabeça da lista.
            self.head = node #Define o node criado como inicio da lista
            for elem in nodes:#loop apartir de todos os elementos do argumento passado
                node.next = Node(data = elem)#cria um novo node que passa a ser o próximo node do anterior
                node = node.next#define como o node atual

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

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

for node in llist:
    print(node)