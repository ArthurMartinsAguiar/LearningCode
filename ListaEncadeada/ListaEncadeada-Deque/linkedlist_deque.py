from collections import deque

'''

'''
def createDeque() -> deque:
    deque_name = deque()
    return deque_name 

def insert_on_deque(deque: deque, value, position = 'head'):
    if position == 'end':
        deque.append(value)
    else:
        deque.appendleft(value)

def pop_from_deque(deque:deque):
    deque.pop()

def main() -> None:
    linkedlist = createDeque()
    positions = ["head","end"]
    while True:
        request = input("[Insert, Pop, Print, Finish]: ")
        match request:
            case "Finish":
                break
            case "Insert":
                value = input("Valor a ser inserido: ")
                position = input("[head, end]: ")
                if position not in positions:
                    print("Insira um posicao disponivel!")
                insert_on_deque(linkedlist, value, position)
            case "Pop":
                pop_from_deque(linkedlist)
            case "Print":
                for i in linkedlist:
                    print(f"{i}")
            case _:
                print("Opcao nao disponivel!")
                continue
                
    

if __name__ == "__main__":
    main()