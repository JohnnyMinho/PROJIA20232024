from Graph import Grafo
from nodo import Node
from XDelta import Xdelta

def imprimir_menu():
    menu = """
    1. Imprimir grafo
    2. Desenhar grafo
    3. Imprimir nodos de grafo
    4. Imprimir arestas de grafo
    5. DFS
    6. BFS
    7. Outra solução
    8. Sair"""
    print(menu)

def main():

    XPress_Delta=Xdelta()
    XPress_Delta.ImplementarGrafo()
    saida = -1

    while saida != 0:

        imprimir_menu()
        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(XPress_Delta.g.m_graph)
            l=input("prima enter para continuar")
        elif saida == 2:
            XPress_Delta.g.desenha()
        elif saida == 3:
            print(XPress_Delta.g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(XPress_Delta.g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            inicio=input("Nodo inicial->")
            fim = input("Nodo final->")
            caminho=XPress_Delta.solucaoDFS( inicio, fim)
            print(caminho)
            if caminho != None:
               a = caminho[0]
               lista=XPress_Delta.imprimeA(a)
               print(lista)
            l = input("prima enter para continuar")
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            caminho=XPress_Delta.solucaoBFS(inicio,fim)
            print(caminho)
            if caminho != None:
                a = caminho[0]
                lista = XPress_Delta.imprimeA(a)
                print(lista)
            l = input("prima enter para continuar")
        elif saida == 7:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            caminho = XPress_Delta.encontraDFS(inicio, fim)
            print(caminho)
            if caminho != None:
                a = caminho[0]
                lista = XPress_Delta.imprimeA(a)
                print(lista)
            l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")






if __name__ == "__main__":
    main()
