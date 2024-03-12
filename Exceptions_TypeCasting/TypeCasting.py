def add_two_numbers(x, y):
    return x + y

def main() -> None:
    '''
    Type Casting é uma manipulação do tipo de dado de uma variavel.
    Ex. int -> str, bool -> str, int -> float.

    Existe duas formas convencionais de type casting, explicitas e
    implicita.

    Implicita - Conversão de tipo realizada pelo próprio compilador. EX:
    '''
    print("Conversão implicita:")
    x = 10 #x == int
    y = 0.75 #y == float
    print("x type: {}, y type: {}".format(type(x), type(y)))
    xy = x * y
    print("xy type: {}".format(type(xy)))
    print("\n")

    '''
    No caso acima, a nova variável auto-denomina do tipo float
    , essa regulação ocorre para armazenar o valor da forma correta,
    de forma que não ocorra perda de memória.
    
    Explicita - Conversão realizada pelo programador para atender requisitos
    de seu algoritmo. A conversão explicita como não é realizada por 'necessidade'
    pode ocorrer a perda de memória. Ex:'''

    print("Conversão explicita: ")
    try:
        resultado = add_two_numbers(1, '2')
    except TypeError as error:
        print("\tTipos de dados heterogeneos (diferentes): ")
        print("\t\t", error)
    else:
        print(f"\tElementos com mesmo tipo de dado, resultado = {resultado}")
    
    '''
    Essa parte do código resulta em um erro, pois a função está tentando
    somar dois dados de tipos diferentes o que gera em um conflito e o código
    é interrompido, caso substitua por dois elementos do mesmo tipo o código
    executa sem problemas e mostra o resultado da equação
    '''
    
if __name__ == "__main__":
    main()