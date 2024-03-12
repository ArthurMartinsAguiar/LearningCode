from collections import deque

'''

'''
def createDeque() -> deque:
    deque_name = deque()
    return deque_name 

def insert_on_deque(deque: deque, value, position = 'head'):
    if position == 'end':
        deque.append(value)
    elif position == 'middle':
        deque.insert(value, len(list)//2)
    else:
        deque.appendleft(value)

def pop_from_deque(deque:deque):
    deque.pop()

def main() -> None:
    #Create a empty linkedList
    linkedList = createDeque()
    positions = ["head","middle","end"]
    run = True
    while run:
        position = input("Where do u wanna insert: ")
        value = input("element: ")
        if position not in positions:
            print("Invalid Position!")
            continue
        
    insert_on_deque(linkedList, value, position)
    print(linkedList)

if __name__ == "__main__":
    main()