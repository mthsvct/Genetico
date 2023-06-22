from populacao import Populacao
import random
import string
import time

class Genetico:

    def __init__(
            self, 
            modelo, 
            tamanho=10, 
            taxaSatisfatoria=80.0,
            numMaxGeracoes=-1
        ):
        self.geracoes = []
        self.taxaSatisfatoria = taxaSatisfatoria
        self.modelo = modelo
        self.tamanho = tamanho
        self.numMaxGeracoes = numMaxGeracoes
        self.cars = string.ascii_letters + string.digits + string.punctuation + ' '
    
    def run(self):
        primeira = Populacao(modelo=self.modelo, tamanho=self.tamanho, individuos=[])
        primeira.cria()
        self.geracoes.append(primeira)

        cont = 1

        print(self.geracoes[-1].melhor_individuo['pctg'])

        while self.geracoes[-1].melhor_individuo['pctg'] < self.taxaSatisfatoria:
            print(f"Geracao {self.geracoes[-1].contador} - Melhor individuo: \"{self.geracoes[-1].melhor_individuo['plv']}\" - {self.geracoes[-1].melhor_individuo['pctg']}%")
            self.selecao()
            self.crossover()
            cont += 1

            if self.numMaxGeracoes != -1 and self.numMaxGeracoes == self.geracoes[-1].contador:
                break
                
            time.sleep(0.1)

        self.resultados(cont)

    def resultados(self, cont):
        print("\n\n")
        print(f"Quantidade de geracoes necessarias: {cont}")
        print(f"Melhor individuo: \"{self.geracoes[-1].melhor_individuo['plv']}\" - {self.geracoes[-1].melhor_individuo['pctg']}%")            

    def selecao(self):
        sel = []
        tam = self.tamanho // 2 if self.tamanho % 2 == 0 else (self.tamanho // 2) + 1
        for i in range(tam):
            ind1 = random.choice(self.geracoes[-1].ranking)
            ind2 = ind1
            while ind2 == ind1:
                ind2 = random.choice(self.geracoes[-1].ranking)
            sel.append([ind1, ind2])
            ind1 = None
            ind2 = None
        self.geracoes[-1].casais = sel
    

    def crossover(self):
        indis = []
        valor = random.randint(1, len(self.modelo)-2)
        
        for casal in self.geracoes[-1].casais:
            plvs = self.cruza(casal, valor)
            indis.append(plvs[0])
            indis.append(plvs[1])
        
        if len(indis) > self.tamanho: indis.pop()
        novosIndis = self.mutacao(indis)
        self.criaPopulacao(novosIndis)
        
    def cruza(self, casal, valor):
        plv1 = self.geracoes[-1].individuos[casal[0]]['plv']
        plv2 = self.geracoes[-1].individuos[casal[1]]['plv']
        novaPlv1 = plv1[:valor] + plv2[valor:]
        novaPlv2 = plv2[:valor] + plv1[valor:]
        return [novaPlv1, novaPlv2]


    def mutacao(self, indis):
        novos = []
        for i in indis:
            lista = list(i)
            for _ in range(1):
                indice = random.randint(0, len(self.modelo)-1)
                lista[indice] = random.choice(self.cars)
            novos.append(''.join(lista))
        return novos


    def criaPopulacao(self, novos):
        nova = Populacao(modelo=self.modelo, tamanho=self.tamanho, individuos=[])
        nova.criaIndividuos(novos)
        self.geracoes.append(nova)


        

        


