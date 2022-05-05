from enum import Enum
import math
import os
import sys
from Mapa import Mapa

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
        self.Objetivos = Objetivos
        self.Rota = []


    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:
            pontos = 10
        elif self.Ambiente.mapa[y][x] == 2:
            pontos = 20
        self.Ambiente.mapa[y][x] = 0
        self.Objetivos.remove((self.y, self.x))
        self.Ambiente.objetosRestante -= 1
        print("Clean")
        return pontos


    def PontoMaisProximo(self):
        MenorDistancia = sys.maxsize
        PontoMaisProximo = None
        print(self.Objetivos)

        for (x,y) in self.Objetivos:
            dist = math.sqrt((x-self.x)**2 + (y-self.y)**2)
            if dist < MenorDistancia:
                PontoMaisProximo = (y,x)
                MenorDistancia = dist

        return PontoMaisProximo

    def AlcancarObjetivo(self, Objetivo):
        if Objetivo == None:
            return None
        x, y = Objetivo
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
        PontoProximo = self.PontoMaisProximo()
        clear = lambda: os.system('cls')
        clear()
        self.AlcancarObjetivo(PontoProximo)

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
Pontos = m1.generate(123)
#m1.renderizar('@','*')

r1 = ReativoBaseadoemObjetivo(m1, Pontos)
r1.executar()
print("Pontuação Final: " , r1.pontuacao)
