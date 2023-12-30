from Encomenda import encomenda

class condutor:

    Veiculos_Disp = {
        'Bicicleta': [5,10],
        'Moto': [20,35]
        #Carga máxima, Velocidade
    }

    def __init__(self,nome,ID,rating = None):
        self.ID = ID
        self.nome = nome
        self.rating = None

    
    def setNewRating(self, rating):
        self.rating = rating
        
