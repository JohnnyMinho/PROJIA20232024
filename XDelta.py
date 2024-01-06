from nodo import Node
from Graph import Grafo
from queue import Queue
from Encomenda import encomenda
from Condutor import condutor
import re

from Condutor import condutor as empregado

class Xdelta:

    def __init__(self):
        self.General_Graph = Grafo(directed = True)
        self.Encomendas = {} # Id_Encomenda : Encomenda
        self.Estafetas = {} # Id_Estafeta : Estafeta
        self.Staff_counter = 1
        self.Package_Counter = 1
    
    def NovaEncomenda(self,id,peso,destino,volume,estado,prazo):
        self.Encomendas[self.Package_Counter] = (encomenda(self.General_Graph,id,peso,destino,volume,estado,prazo,self.ID,None,None))
        #self,id,peso,destino,volume,estado,prazo,ID_Estafeta,veiculo,start,grafo,rating = None,custo = None

    def NovoEmpregado(self,nome):
        self.Estafetas[self.Staff_counter] = (condutor(nome,self.Staff_counter,None))
    
    def ImplementarGrafo(self):
        filename = "Ruas.txt"
        ruas = {}
        
        with open(filename) as f:
            for line in f:
                match = re.match(r'"([^"]*)".*\[([^\]]*)\]', line)
                if match:
                    nome_rua = match.group(1)
                    neighbors = match.group(2).split(')(')
                    ruas[nome_rua] = []  # Initialize the list for each street if not present
                    for neighbor in neighbors:
                        neighbor_name, price = neighbor.split(',')
                        ruas[nome_rua].append({'neighbor_name': neighbor_name, 'price': int(price.strip(")"))})

        for rua, vizinhos in ruas.items():
            for neighbor in vizinhos:
                self.General_Graph.add_edge(rua, neighbor['neighbor_name'], neighbor['price'])