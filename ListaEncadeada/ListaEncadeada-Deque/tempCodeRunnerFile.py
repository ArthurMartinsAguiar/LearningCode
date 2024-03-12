from collections import deque

'''
Features of deque.
'''
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

