from nodo import Node
from Graph import Grafo
from queue import Queue
from Encomenda import encomenda
from Condutor import condutor
import re
import datetime

from Condutor import condutor as empregado

class Xdelta:

    #A empresa é sediada na Rua do Fiado
    ruas_disp = []

    def __init__(self):
        self.General_Graph = Grafo(directed = True)
        self.Encomendas = {} # Id_Encomenda : Encomenda
        self.Estafetas = {} # Id_Estafeta : Estafeta
        self.Staff_counter = 1
        self.Package_Counter = 1

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
                self.ruas_disp.append(rua)
                self.General_Graph.add_edge(rua, neighbor['neighbor_name'], neighbor['price'])

    def AdicionarEncomenda(self):
        filename = "Encomendas.txt"
        print("Digite as seguintes informações com exatamente o seguinte formato peso,destino,ID_condutor,prazo(epoch):")
        saida = (input(""))
        encomenda_valida = 1
        entry_parts = saida.split(',')
        self.Package_Counter = self.Package_Counter+1
        ID = self.Package_Counter
        peso = int(entry_parts[0])
        if(peso>20 or peso < 0):
            print("Peso Inválido")
            encomenda_valida = 0
        if(peso > 5):
            veiculo = "Moto"
        elif(peso <=5):
            veiculo = "Bicicleta"
        destino = entry_parts[1]
        if(destino not in self.ruas_disp):
            print("Esta Rua não existe")
            encomenda_valida = 0
        volume = 0
        ID_condutor = int(entry_parts[2])
        epoch_time = int(entry_parts[3])
        status = 0
        
        if(encomenda_valida == 1):
            self.Encomendas[ID] = encomenda(ID,peso,destino,volume,status,epoch_time,ID_condutor,veiculo,self.General_Graph)
            with open(filename, 'a') as file:
                file.write(f"{ID},{peso},{destino},{volume},{status},{epoch_time},{ID_condutor},{veiculo}\n")
            
            self.Encomendas[ID] = encomenda(ID,peso,destino,volume,status,epoch_time,ID_condutor,veiculo,self.General_Graph)

            if(ID_condutor in self.Estafetas.keys()):
                estafeta = self.Estafetas[ID_condutor]
                estafeta.adicionar_encomenda(self.Encomendas.get(ID))
                estafeta.organizaportempo()

        else:
            print("Encomenda inválida")

        

    def CarregarEncomendas(self):
        filename = "Encomendas.txt"

        with open(filename) as f:
            for line in f:
                self.Package_Counter = self.Package_Counter+1
                entry_parts = line.split(',')

                # Extract individual pieces of information
                ID = int(entry_parts[0])
                peso = int(entry_parts[1])
                destino = entry_parts[2]
                volume = int(entry_parts[3])
                status = int(entry_parts[4])
                epoch_time = int(entry_parts[5])
                ID_condutor = int(entry_parts[6])
                vehicle_type = entry_parts[7].strip()

                # Convert epoch time to a datetime object
                timestamp = datetime.datetime.utcfromtimestamp(epoch_time)

                self.Encomendas[ID] = encomenda(ID,peso,destino,volume,status,epoch_time,ID_condutor,vehicle_type,self.General_Graph)

                if(ID_condutor in self.Estafetas.keys()):
                    estafeta = self.Estafetas[ID_condutor]
                    estafeta.adicionar_encomenda(self.Encomendas.get(ID))
                    estafeta.organizaportempo()

    def CarregarEstafetas(self):
        filename = "Estafetas.txt"

        with open(filename) as f:
            for line in f:
                self.Staff_counter = self.Staff_counter+1
                entry_parts = line.split(',')

                # Extract individual pieces of information
                nome = entry_parts[0]
                id = int(entry_parts[1])
                pos_inicial = entry_parts[2]

                # Convert epoch time to a datetime object

                self.Estafetas[id] = condutor(nome,id,pos_inicial)
                

    def AdicionarEstafeta(self):

        print("Digite as seguintes informações com exatamente o seguinte formato nome:")
        saida = (input(""))
        filename = "Estafetas.txt"
        entry_parts = saida.split(',')
        ID = self.Package_Counter
        nome = entry_parts[0]
        
        self.Estafetas[ID] = condutor(nome,ID,"Rua do Fiado")
        with open(filename, 'a') as file:
                file.write(f"{nome},{ID},Rua do Fiado\n")

    #Funções de auxilio aos algoritmos

    def organizar_percurso(self):
        #Função que auxilia com a organização de um percurso para o estafeta tendo em conta a prioridade de cada encomenda
        #Esta função não têm interesse em maximizar a carga de cada veículo antes da saída sendo que a partir do momento que não há maneira de respeitar
        #As regras impostas (encomendas ou peso acumulado para o veículo em causa), este é expedido.
        start_inicial = "Rua do Fiado"
        lista_percurso = []
        peso_acumulado = 0
        veiculo_anterior = []

        for key, object in self.Estafetas.items():
            for encomenda in self.Estafetas[key].encomendas:
                veiculos_disp = self.Estafetas[key].Veiculos_Disp
                #As encomendas já estão organizadas por ordem de prioridade, logo apenas é preciso as organizar segundo o veículo e o peso
                #Caso n encomendas seguidas sejam realizadas no mesmo veículo, estas podem ser feitas seguidamente
                #Caso uma encomenda tenha um veículo diferente da anterior, o estafeta vai ter de voltar à estação de recolha na Rua do Fiado
                #Uma solução para este problema seria verificar se o Estafa teria uma vantagem em agrupar o maior número possível de encomendas no veículo
                #Esta solução seria viável se o número de encomendas que poderiam ficar em atraso fosse reduzido.

                peso_encomenda = encomenda.peso
                veiculo_atual = veiculos_disp[encomenda.transporte] #Para nos facilitar a vida ficamos com os dados do veículo, se for uma Moto ficamos com [20,35], uma bicicleta [5,10]
                #Basicamente para ver o peso máximo fazemos veículo_atual[0], para a velocidade é veículo_atual[1]
                if(veiculo_atual == veiculo_anterior):
                    #Se o veículo for igual ao que vai usado para a encomenda anterior, podemos tentar acumular outra encomenda
                    if(peso_acumulado + peso_encomenda > veiculo_atual[0]):
                        #O peso acumulado no veículo excede a capacidade máxima, logo ele prossegue para as entregas e depois vai ter de voltar ao local de recolha
                        lista_percurso.append("Rua do Fiado")
                        lista_percurso.append(encomenda.destino)
                        peso_acumulado = 0
                    elif(peso_acumulado + peso_encomenda < veiculo_atual[0]):
                        #O peso acumulado ainda não atingiu o peso limite do veículo, logo podemos aproveitar e levar mais encomendas
                        lista_percurso.append(encomenda.destino)
                        peso_acumulado = peso_acumulado+peso_encomenda
                else:
                    #O veículo é diferente do anterior.
                    lista_percurso.append("Rua do Fiado")
                    lista_percurso.append(encomenda.destino)
                    peso_acumulado = 0 
                    peso_acumulado = peso_acumulado+peso_encomenda #Como vamos trocar o veículo temos de reniciar o peso
                
        return lista_percurso

