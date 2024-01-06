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
    7. A* Estrela
    8. Greedy
    9. Adicionar Estafeta
    10. Nova Encomenda
    0. Sair"""
    print(menu)

def main():

    XPress_Delta=Xdelta()
    XPress_Delta.ImplementarGrafo()
    XPress_Delta.CarregarEncomendas()
    XPress_Delta.CarregarEstafetas()
    saida = -1

    while saida != 0:

        imprimir_menu()
        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(XPress_Delta.General_Graph.m_graph)
            l=input("prima enter para continuar")
        elif saida == 2:
            XPress_Delta.General_Graph.desenha()
        elif saida == 3:
            print(XPress_Delta.General_Graph.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(XPress_Delta.General_Graph.imprime_aresta())
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
        elif saida == 8:
            print("TO DO")
        elif saida == 9:
            XPress_Delta.AdicionarEstafeta()
        elif saida == 10:
            XPress_Delta.AdicionarEncomenda()
        else:
            print("NENHUMA OPÇÃO SELECIONADA")
            l = input("prima enter para continuar")

if __name__ == "__main__":
    main()
