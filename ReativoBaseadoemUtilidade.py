import os
from numpy import empty
from Mapa import Mapa
import numpy as np
import time

class ReativoBaseadoemUtilizade:
    # O Agente Baseado em utilidade irá utilizar os objetivos também como lista de utilidade 
    # A lista de objetivos deve ser passada de uma forma específica para isso
    # Os pontos de maior utilidade devem ser colocados nas primeiras posições e os de menor utilidade nas ultimos
    # Portanto, temos uma lista de objetivos em ordem decrescente de utilidade
    def __init__(self, Mapa, Objetivos):
        self.x = 0
        self.y = 0
        self.Ambiente = Mapa
        self.pontuacao = 0
        self.Objetivos = Objetivos


    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:
            pontos = 10
        elif self.Ambiente.mapa[y][x] == 2:
            pontos = 20
        self.Ambiente.mapa[y][x] = 0
        self.Ambiente.objetosRestante -= 1
        return pontos


    def VerficaObjeto(self, ListadeObejetosPossiveis):
        for objeto in ListadeObejetosPossiveis:
            if self.Ambiente.mapa[self.y][self.x] == objeto:
                return True
        return False

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
        y, x = Objetivo
        while(self.x < x):
            self.x +=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
                self.Objetivos = list(filter((self.y, self.x).__ne__, self.Objetivos))
            self.Render()
        while(self.x > x):
            self.x -=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
                self.Objetivos = list(filter((self.y, self.x).__ne__, self.Objetivos))
            self.Render()
        while(self.y < y):
            self.y +=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
                self.Objetivos = list(filter((self.y, self.x).__ne__, self.Objetivos))
            self.Render()
        while(self.y > y):
            self.y -=1
            if self.VerficaObjeto([1,2]):
                self.pontuacao += self.Clean(self.x,self.y)
                self.Objetivos = list(filter((self.y, self.x).__ne__, self.Objetivos))
            self.Render()

    #Função de setar o proximo objetivo e ir até ele
    def MovimentaObjetivo(self):
        print(self.Objetivos)
        ProximoPonto = self.Objetivos.pop(0)    #Retira o primeiro elemento da lista de objetivos. Isto é, pois a lista de utilizades é a lista de objetivos.
        print(ProximoPonto)
        self.AlcancarObjetivo(ProximoPonto)     #Se movimenta até o proximo objetivo

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
    r1 = ReativoBaseadoemUtilizade(m1, Pontos)
    r1.executar()
    fim = time.process_time()
    Tempos.append(fim-inicio)

Tempos = np.array(Tempos)

clear = lambda: os.system('cls')
clear()
print("Baseado em Objetivos")
print("Tempos: ", Tempos)
print("Media: ", np.mean(Tempos), "s(+-) ", np.std(Tempos))      