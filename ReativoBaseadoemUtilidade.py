from enum import Enum
import math
import os
import sys

from numpy import empty
from Mapa import Mapa

class Movimento(Enum):
    Cima  = 1
    Baixo = 2
    Esquerda = 3
    Direita = 4
      
class ReativoBaseadoemUtilizade:
    
    def __init__(self, Mapa, Objetivos, randomMov= True):
        self.randomMov = randomMov
        self.x = 0
        self.y = 0
        self.sentido = "direita"
        self.Ambiente = Mapa
        self.pontuacao = 0
        self.Objetivos = Objetivos
        self.Rota = []


    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:
            pontos = 10
        elif self.Ambiente.mapa[y][x] == 2:
            pontos = 20
        self.Ambiente.mapa[y][x] = 0
        self.Ambiente.objetosRestante -= 1
        print("Clean")
        return pontos

    def AlcancarObjetivo(self, Objetivo):
        if Objetivo == None:
            return None
        y, x = Objetivo
        while(self.x < x):
            self.x +=1
            if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
                self.pontuacao += self.Clean(self.x,self.y)
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)
        while(self.x > x):
            self.x -=1
            if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
                self.pontuacao += self.Clean(self.x,self.y)
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)

        while(self.y < y):
            self.y +=1
            if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
                self.pontuacao += self.Clean(self.x,self.y)
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)

        while(self.y > y):
            self.y -=1
            if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
                self.pontuacao += self.Clean(self.x,self.y)
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)
            
    def MovimentaObjetivo(self):
        ProximoPonto = self.Objetivos.pop(0)
        clear = lambda: os.system('cls')
        clear()
        print(ProximoPonto)

        self.AlcancarObjetivo(ProximoPonto)

    def ObjectiveMovimentation(self):
        print("Localidade: " , self.Ambiente.mapa[self.y][self.x])
        if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
            self.pontuacao += self.Clean(self.x,self.y)
            self.MovimentaObjetivo()
        else:
            self.MovimentaObjetivo()

    def executar(self):
        while self.Ambiente.objetosRestante > 0:
            clear = lambda: os.system('cls')
            clear()
            self.Ambiente.renderizar('@','#','', X_Agente = self.x, Y_Agente = self.y)
            self.ObjectiveMovimentation()

            
            
m1 = Mapa(m=20, n=20)
ListadeUtilizades = m1.generate(123)
#m1.renderizar('@','*')

r1 = ReativoBaseadoemUtilizade(m1, ListadeUtilizades)
r1.executar()
print("Pontuação Final: " , r1.pontuacao)
