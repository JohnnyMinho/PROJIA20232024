from nodo import Node
from Graph import Grafo
from queue import Queue

class encomenda:

    def __init__(self,id,peso,destino,volume,estado,prazo,ID_Estafeta,veiculo,start,grafo,rating = None,custo = None):
        self.graph = grafo
        self.id = id
        self.peso = peso
        self.destino = destino
        self.rating = None
        self.custo = None
        self.volume = volume
        self.estado = estado
        self.prazo = prazo
        self.ID_estafeta = ID_Estafeta
        self.transporte = veiculo
        self.start = start #O start segundo o inunciado é sempre a central de estafetas

    def RatingEncomenda(self,rating):
        self.rating = rating
    
    def SetCusto(self,custo):
        self.custo = custo

    def SetEstado(self,estado):
        #Só tem dois estados, em progresso e concluida
        self.estado = estado

    def getRating(self):
        return self.rating
    
