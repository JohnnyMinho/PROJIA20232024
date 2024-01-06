from Encomenda import encomenda

class condutor:

    Veiculos_Disp = {
        'Bicicleta': [5,10],
        'Moto': [20,35]
        #Carga máxima, Velocidade
    }

    def __init__(self,nome,ID,ultima_pos,veiculo,peso_total,rating = None):
        self.ID = ID
        self.nome = nome
        self.rating = None
        self.ultima_pos = ultima_pos
        self.veiculo_atual = None
        self.peso_total = 0
        self.encomendas = []

    def setNewRating(self, rating):
        self.rating = rating
        
    def NovaPos(self, pos):
        self.ultima_pos = pos
    
    def adicionar_encomenda(self, encomenda):
        self.encomendas.append(encomenda)
    
    def setVeiculo(self,veiculo):
        if(veiculo in self.Veiculos_Disp):
            self.veiculo_atual = veiculo

