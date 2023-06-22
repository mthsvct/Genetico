from populacao import Populacao

class Genetico:


    def __init__(self, modelo, taxaSatisfatoria=80.0):
        self.geracoes = []
        self.taxaSatisfatoria = taxaSatisfatoria
        self.modelo = modelo
    
    def run(self):
        primeira = Populacao(modelo=self.modelo)
        primeira.cria()
        self.geracoes.append(primeira)
        """ while True:
            pass """
            
    
    def selecao(self):
        pass
        

        


