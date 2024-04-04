'''No caso anterior na classe Node você conseguia ver que existia
dois elementos principais'''

'''Adicionar o método __repr__ em ambas as classes pode ajudar 
com a representação daquele objeto.
O método __repr__: it's meant to return an unambiguous string representation of an object 
that can be used to reproduce the same object when fed to the eval() function

Traduzindo: O método retorna o conteúdo daquele objeto no formato de strings. Isso pode ser usado para reproduzir o mesmo objeto
quando alimentado para a função eval() 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    
    
'''Olhe um exemplo que utiliza as classes acima para implementar uma lista encadeada com três nodes'''

llist = LinkedList()
primeiro_node = Node("a")
llist.head = primeiro_node
segundo_node = Node("b")
primeiro_node.next = segundo_node
terceiro_node = Node("c")
segundo_node.next = terceiro_node

'''Ao associar o primeiro node com o inicio da lista, basta associar os nodes seguintes ao primeiro node
que ambos serão representados como parte da lista'''

print(llist)