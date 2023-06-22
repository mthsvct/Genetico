import random
import string
from enchant.utils import levenshtein

class Populacao:

    contador = 0

    def __init__(self, modelo, tamanho=10, individuos=[]):
        self.individuos = individuos
        self.tamIndi = len(modelo)
        self.aptidao = 0.0
        self.tamanho = tamanho
        self.melhor_individuo = None
        self.pior_individuo = None
        self.media = 0.0
        self.modelo = modelo
        self.ranking = []
        self.casais = []
        self.contador = Populacao.contador
        Populacao.contador += 1
        self.cars = string.ascii_letters + string.digits + string.punctuation + ' '
    
    def __str__(self):
        return "População com {} indivíduos".format(self.tamanho)
    
    # Cria uma palavra aleatória.
    def criaPlv(self): return ''.join(random.choice(self.cars) for _ in range(self.tamIndi))

    # Cria uma população inicial
    def cria(self):
        while self.zerado():
            for _ in range(self.tamanho):
                porcentagem = 0.0
                while porcentagem == 0.0:
                    palavra = self.criaPlv()
                    porcentagem = self.calcula(palavra)
                self.individuos.append({'plv': palavra, 'pctg': porcentagem })
        self.atualizaDados()
        self.getRankPropRanking()

    # Calcula a porcentagem de proximidade do modelo com o individuo
    def calcula(self, palavra):
        comp = levenshtein(palavra, self.modelo)
        r = ((self.tamIndi - comp) / self.tamIndi) * 100
        return r

    def calculaTodos(self):
        for i in self.individuos:
            i['pctg'] = self.calcula(i['plv'])
    
    def criaIndividuos(self, listaPlvs):
        for plv in listaPlvs:
            self.individuos.append({'plv': plv, 'pctg': self.calcula(plv)})
        self.atualizaDados()

        """ if self.contador < 100:
            self.getRankPropFitness()
        else:
            self.getRankPropRanking() """
        self.getRankPropRanking()

    # Atualiza indormações dos cálculos de porcentagem
    def atualizaDados(self):
        self.individuos.sort(key=lambda x: x['pctg'], reverse=True)
        self.aptidao = sum([i['pctg'] for i in self.individuos]) / len(self.individuos)
        self.melhor_individuo = self.individuos[0]
        self.pior_individuo = self.individuos[-1]

    # Retorna a quantidade de itens que possuem 0% de aptidão.    
    def qntZero(self):
        return len([i['pctg'] for i in self.individuos if i['pctg'] == 0.0])

    # Retorna true se todos os itens estiverem zerados.
    def zerado(self):
        r = True
        if len(self.individuos) > 0:
            r = self.qntZero() == self.tamanho
        return r

    # Monta o ranking a partir do valor de fitness;
    def getRankPropFitness(self):
        self.ranking = []
        for index, i in enumerate(self.individuos):
            for _ in range(int(i['pctg'])):
                self.ranking.append(index)

    # Monta o ranking adicionando pesos pela a ordem do valor do fitness.
    def getRankPropRanking(self):
        p = [50, 30, 10, 5, 1, 1, 1, 1, 1]
        ranking = []
        index = 0
        self.ranking = []
        for i in p:
            for _ in range(i):
                ranking.append(index)
            index += 1
        self.ranking = ranking





    