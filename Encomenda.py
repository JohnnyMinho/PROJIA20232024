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
        self.caminho = []
        self.Ultimo_Metodo_Usado = ""
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

    def SetCaminho(self, caminho):
        self.caminho = caminho

    def MetodoUsado(self, metodo):
        self.Ultimo_Metodo_Usado = metodo

    def ImprimirInfo(self):
        print("ID->"+str(self.id))
        print("Peso->"+str(self.peso))
        print("Destino->"+self.destino)
        print("Custo->"+str(self.custo))
        if(self.estado == 1):
            print("Estado->"+ str(self.estado) + ", Entregue")
        elif(self.estado == 2):
            print("Estado->" + str(self.estado) + ", Erro na Entrega")
        elif(self.estado == 0):
            print("Estado->" + str(self.estado) + ", Por entregar")
        if(self.rating == 0):
            print("Rating->"+str(self.rating)+" Entregue fora de prazo/Encomenda Não entregue")
        elif(self.rating == 1):
            print("Rating->"+str(self.rating)+" Entregue dentro do prazo")
        print("ID_Estafeta->"+str(self.ID_estafeta))
        print("Veículo usado ->"+self.transporte)
        print("Caminho usado para a Entrega -> " + str(self.caminho))
        print("Ultimo Algoritmo Usado ->"+ self.Ultimo_Metodo_Usado + '\n')