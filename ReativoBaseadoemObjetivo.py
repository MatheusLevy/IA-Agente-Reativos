from enum import Enum
import math
import os
import sys
from Mapa import Mapa
import numpy as np
import time

class Movimento(Enum):
    Cima  = 1
    Baixo = 2
    Esquerda = 3
    Direita = 4
      
class ReativoBaseadoemObjetivo:
    
    def __init__(self, Mapa, Objetivos, randomMov= True):
        self.randomMov = randomMov
        self.x = 0
        self.y = 0
        self.sentido = "direita"
        self.Ambiente = Mapa
        self.pontuacao = 0
        self.Objetivos = Objetivos  #Lista de Objetivos
        self.Rota = []


    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:
            pontos = 10
        elif self.Ambiente.mapa[y][x] == 2:
            pontos = 20
        self.Ambiente.mapa[y][x] = 0
        self.Objetivos.remove((self.y, self.x)) #Ao encontrar um objetivo remove ele da lista de objetivos
        self.Ambiente.objetosRestante -= 1
        return pontos

    #Calcula a distacia entre a localização do agente e o objetivo mais proximo 
    #Utilizando a equação da menor distancia entre dois pontos em um plano cartesiano
    def PontoMaisProximo(self):
        MenorDistancia = sys.maxsize    #Inicializa a menor distancia como um valor muito grande 
        PontoMaisProximo = None         #Inicializa o Ponto Mais Proximo como Nenhum
        print(self.Objetivos)

        for (x,y) in self.Objetivos:
            dist = math.sqrt((x-self.x)**2 + (y-self.y)**2)
            if dist < MenorDistancia:
                PontoMaisProximo = (y,x)
                MenorDistancia = dist

        return PontoMaisProximo

    def VerficaObjeto(self, ListadeObejetosPossiveis):
        for objeto in ListadeObejetosPossiveis:
            if self.Ambiente.mapa[self.y][self.x] == objeto:
                return True
        return False
    #Função que limpa a tela e renderiza o mapa
    def Render(self):
        clear = lambda: os.system('cls')
        clear()
        self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)
    
    # Função para Alcançar um Objetivo
    # @Parametros:
    # Objetivo: Um ponto(x,y)
    # A função move o agente até a mesma coluna que o objetivo
    # e depois move até a mesma linha que o objetivo
    def AlcancarObjetivo(self, Objetivo):
        if Objetivo == None:
            return None
        x, y = Objetivo
        while(self.x < x):
            self.x +=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
            self.Render()
        while(self.x > x):
            self.x -=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
            self.Render()
        while(self.y < y):
            self.y +=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
            self.Render()
        while(self.y > y):
            self.y -=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
            self.Render()

    def MovimentaObjetivo(self):
        PontoProximo = self.PontoMaisProximo()
        #clear = lambda: os.system('cls')
        #clear()
        self.AlcancarObjetivo(PontoProximo)

    def ObjectiveMovimentation(self):
        if self.VerficaObjeto([1,2]):
            self.pontuacao += self.Clean(self.x,self.y)
        else:
            self.MovimentaObjetivo()
        
    def executar(self):
        while self.Ambiente.objetosRestante > 0:
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)
            self.ObjectiveMovimentation()

            
            
Tempos = []
for _ in range(5):   
    m1 = Mapa(m=20, n=20)
    Pontos = m1.generate(123456)
    inicio = time.process_time()
    r1 = ReativoBaseadoemObjetivo(m1, Pontos)
    r1.executar()
    fim = time.process_time()
    Tempos.append(fim-inicio)

Tempos = np.array(Tempos)

clear = lambda: os.system('cls')
clear()
print("Baseado em Objetivos")
print("Tempos: ", Tempos)
print("Media: ", np.mean(Tempos), "s(+-) ", np.std(Tempos))

