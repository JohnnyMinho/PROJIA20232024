from Graph import Grafo
from nodo import Node
from XDelta import Xdelta

import os

#As heuristicas dos nossos caminhos são basicamente atalhos e caminhos novos ou antigos que foram sendo feitos ou extintos e ainda não estou presentes aqui
#Como as heuristicas derivam de experiências anteriores, este modo de utilizar as heuristicas é assumido como válido
#Os valores usados são uma "média" de todos os valores de ruas com várias entradas
#As ruas com menos entradas ou com valores pequenos têm heuristicas com valores ligeiramente mais baixos que 1 ou 2 ruas presentes
#Contudo esta não é a regra para todos porque ruas novas a serem construidas podem implicar uma heuristica maior

def imprimir_menu():
    menu = """
    XPRESS-DELTA TERMINAL 1.0

    |1. Imprimir grafo           |
    |2. Desenhar grafo           |
    |3. Imprimir nodos de grafo  |
    |4. Imprimir arestas de grafo|
    |5. DFS                      |
    |6. BFS                      |
    |7. Greedy                   |
    |8. A* Estrela               |
    |9. Adicionar Estafeta       |
    |10. Nova Encomenda          |
    |11. Ver Encomendas          |
    |12. Ver Estafetas           |
    |0. Sair                     |
    """
    print(menu)

def main():

    XPress_Delta=Xdelta()
    XPress_Delta.ImplementarGrafo()
    XPress_Delta.CarregarEstafetas()
    XPress_Delta.CarregarEncomendas()
    saida = -1

    while saida != 0:
        os.system("clear")
        imprimir_menu()
        saida = int(input("    introduza a sua opcao-> "))
        os.system("clear")
        if saida == 0:
            print("Shutting Down")
        elif saida == 1:
            print(XPress_Delta.General_Graph.m_graph)
            l=input("prima enter para continuar")
        elif saida == 2:
            XPress_Delta.General_Graph.desenha()
            l=input("prima enter para continuar")
        elif saida == 3:
            print(XPress_Delta.General_Graph.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(XPress_Delta.General_Graph.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            caminho=XPress_Delta.SolucaoDFS()
            #Quando um caminho indica None é porque o algoritmo errou por alguma razão e a encomenda não é entregue
            l = input("prima enter para continuar")
        elif saida == 6:
            caminho=XPress_Delta.SolucaoBFS()
            l = input("prima enter para continuar")
        elif saida == 7:
            caminho = XPress_Delta.SolucaoGreedy()
            l = input("prima enter para continuar")
        elif saida == 8:
            caminho = XPress_Delta.SolucaoA()
            l = input("prima enter para continuar")
        elif saida == 9:
            XPress_Delta.AdicionarEstafeta()
        elif saida == 10:
            XPress_Delta.AdicionarEncomenda()
        elif saida == 11:
            XPress_Delta.VerEncomendas()
        elif saida == 12:
            XPress_Delta.VerEstafetas()
        else:
            print("NENHUMA OPÇÃO SELECIONADA")
            l = input("prima enter para continuar")

if __name__ == "__main__":
    main()
