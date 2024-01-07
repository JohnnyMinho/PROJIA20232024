from nodo import Node
from Graph import Grafo
from queue import Queue

class encomenda:

    def __init__(self,id,peso,destino,volume,estado,prazo,ID_Estafeta,veiculo,grafo,rating = None,custo = None):
        self.graph = grafo
        self.id = id
        self.peso = peso
        self.destino = destino
        self.rating = None
        self.custo = None
        self.volume = volume #Como o volume ainda não têm uso vamos deixar sempre este valor a 0, ou simplesmente não o temos em consideração
        self.estado = estado
        self.prazo = prazo #Vai usar o calendário gregório 
        self.ID_estafeta = ID_Estafeta
        self.transporte = veiculo
        self.start = None #O start da primeira encomenda do estafeta é sempre o 

    def RatingEncomenda(self,rating):
        self.rating = rating
    
    def SetCusto(self,custo):
        self.custo = custo

    def SetEstado(self,estado): 
        #Só tem dois estados, em progresso e concluida -> 0 e 1 respetivamente
        self.estado = estado

    def getRating(self):
        return self.rating
    
    def setStart(self,start):
        self.start = start

    def ImprimirInfo(self):
        print("ID->"+self.id)
        print("Peso->"+self.peso)
        print("Destino->"+self.destino)
        print("Custo->"+self.custo)
        if(self.estado == 1):
            print("Estado->"+self.estado + ", Entregue")
        elif(self.estado == 2):
            print("Estado->" + self.estado + ", Erro na Entrega")
        elif(self.estado == 0):
            print("Estado->" + self.estado + ", Por entregar")
        if(self.rating == 0):
            print("Rating->"+self.rating+"Entregue dora de prazo")
        elif(self.rating == 0):
            print("Rating->"+self.rating+"Entregue dentro do prazo")
        print("ID_Estafeta->"+self.ID_estafeta)
        printf("Veículo usado ->"+self.transporte)