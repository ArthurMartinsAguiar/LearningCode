from collections import deque

'''
Stacks ou pilhas se baseiam no argortimo FILO (First in, Last out),
isso significa que o primeiro elemento a entrar será o ultimo a sair.
Pilhas são conhecidas por ser empilhamento de coisas, sendo um algoritmo
muito utilizado em processos.
'''

def printing(stack: deque):
    print("\n")
    for i in range(len(stack)):
        print(f"{stack[i]}")

stack = deque()

for i in range(1, 6):
    stack.append("🟫" * i)
print(stack)

stack.reverse() #Como a lista foi revertida, o ultimo elemento inserido passa a ser o primeiro.
printing(stack)

while True:
    if len(stack) == 0:
        break
    stack.popleft()#Retira o ultimo elemento inserido
    printing(stack)
    
