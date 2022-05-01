from asyncio.windows_events import NULL
from enum import Enum
import os
import random
from time import sleep
from Mapa import Mapa

class Movimento(Enum):
    Cima  = 1
    Baixo = 2
    Esquerda = 3
    Direita = 4
      
class ReativoSimples:
    
    def __init__(self, Mapa, randomMov= True):
        self.randomMov = randomMov
        self.x = 0
        self.y = 0
        self.Ambiente = Mapa

    def Clean(self, x, y):
        self.Ambiente.mapa[y][x] = 0
        self.Ambiente.objetosRestante -= 1
        print("Clean")

    def Movimenta(self):
        mv = random.choice(list(Movimento))
        print(mv)
        if mv == Movimento.Cima:
            if self.y - 1 >= 0:
                self.y -= 1
                  
        elif mv == Movimento.Baixo:
            if self.y + 1 < self.Ambiente.m :
                self.y += 1
                  
        elif mv == Movimento.Esquerda:
            if self.x - 1 >= 0:
                self.x -= 1
                   
        elif mv == Movimento.Direita:
            if self.x + 1 < self.Ambiente.n:
                self.x += 1
        


    def RandomMovimentation(self):
        print("Localidade: " , self.Ambiente.mapa[self.y][self.x])
        if self.Ambiente.mapa[self.y][self.x] == 1:
            self.Clean(self.x,self.y)
            self.Movimenta()
        else:
            self.Movimenta()

    def executar(self):
        while self.Ambiente.objetosRestante > 0:
            clear = lambda: os.system('cls')
            clear()
            print("obj " , self.Ambiente.objetosRestante)
            print("SelfX = ", self.x)
            print("SelfY = ", self.y )
            self.Ambiente.renderizar('@','*', X_Agente = self.x, Y_Agente = self.y)
            self.RandomMovimentation()
            input("Press Enter to continue...")
    
            
            
m1 = Mapa(m=5, n=5,objetos=10)
m1.generate(123)
#m1.renderizar('@','*')

r1 = ReativoSimples(m1)
r1.executar()
