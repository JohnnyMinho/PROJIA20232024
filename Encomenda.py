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