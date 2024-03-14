from collections import deque

'''
Features of deque.
'''
def main() -> None:
    
    #Create a deque list.
    list = deque()
    
    #deque.append inserts a element in the end of the list.
    print("Append Insertions:")
    list.append('first')
    list.append('second')
    list.append('third')
    print(list,"\n")
    
    #deque.appendleft insert a element in the begnning of the list.
    print("Insert on head:")
    list.appendleft('-')
    list.appendleft('podium')
    print(list,"\n")
    
    #deque.clear clear the list.
    print('Clear the list:')
    list.clear()
    print(list, "\n")
    
    #deque.copy make a original list copy
    for i in range(0,10):
        if i % 2 == 0:
            list.append(f'{i}')
        else:
            list.appendleft(f'{i}')
    print('Copy list:')
    copy_list = list.copy()
    print(f"Original list: {list}")
    print(f"Copy list : {copy_list}\n")
    
    #deque.count Count repetitions of a element
    from random import randint
    list.clear()
    running = True
    while running:
        list.append(randint(1,3))
        if list.__len__() == 10:
            running = False
    print(f'List :{list}')
    for i in set(list):
        print(f'Count of {i} elements: {list.count(i)}')
    print('\n')

    '''
    Caso deseje saber mais sobre deque, pesquise sua documentação...Lá tem todos os exemplos
    e modo de uso.
    '''

if __name__ == "__main__":
    main()