from enum import Enum
import os
import random
from Mapa import Mapa

class Movimento(Enum):
    Cima  = 1
    Baixo = 2
    Esquerda = 3
    Direita = 4
      
class ReativoBaseadoemModelo:
    
    def __init__(self, Mapa, randomMov= True):
        self.randomMov = randomMov
        self.x = 0
        self.y = 0
        self.sentido = "direita"
        self.Ambiente = Mapa
        self.pontuacao = 0
        self.Historico = []
        self.UltimoEstado = (0,0)
    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:
            pontos = 10
        elif self.Ambiente.mapa[y][x] == 2:
            pontos = 20
        self.Ambiente.mapa[y][x] = 0
        self.Ambiente.objetosRestante -= 1
        print("Clean")
        return pontos

    def checaPreso(self):
        if self.x - 1 >= 0:
            if (self.x-1,self.y) not in self.Historico:
                return False
                
        if self.x + 1 < self.Ambiente.n:
            if(self.x+1, self.y) not in self.Historico:
                return False
        if self.y - 1 >= 0:
            if (self.x, self.y-1) not in self.Historico:
                return False
        if self.y + 1 < self.Ambiente.m:
            if(self.x, self.y+1) not in self.Historico:
                return False
        
        return True

    def validaMovimento(self, x_next, y_next):
        if (x_next, y_next) in self.Historico and not self.checaPreso():
            return False
        return True

    def MovimentaRandom(self):
        self.Historico.append((self.x,self.y))
        mv = random.choice(list(Movimento))
        print(mv)

        if mv == Movimento.Cima:
            if self.y - 1 >= 0:
                if self.validaMovimento(self.x, self.y-1):
                    self.y -= 1
                  
        elif mv == Movimento.Baixo:
            if self.y + 1 < self.Ambiente.m :
                if self.validaMovimento(self.x, self.y+1):
                    self.y += 1
                  
        elif mv == Movimento.Esquerda:
            if self.x - 1 >= 0:
                if self.validaMovimento(self.x-1,self.y):
                    self.x -= 1
                   
        elif mv == Movimento.Direita:
            if self.x + 1 < self.Ambiente.n:
                if self.validaMovimento(self.x+1, self.y):
                    self.x += 1

    def MovimentaLinha(self):
        if self.sentido == "direita":
            if (self.x + 1 < self.Ambiente.n):
                self.x +=1
            else:
                if(self.y + 1 < self.Ambiente.m):
                    self.y +=1
                    self.sentido = "esquerda"

        elif self.sentido == "esquerda":
            if(self.x -1 >= 0):
                self.x -=1
            else:
               if(self.y + 1 < self.Ambiente.m):
                    self.y +=1
                    self.sentido = "direita"


    def RandomMovimentation(self):
        print("Localidade: " , self.Ambiente.mapa[self.y][self.x])
        if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
            self.pontuacao += self.Clean(self.x,self.y)
            self.MovimentaRandom()
        else:
            self.MovimentaRandom()

    def LinhaMovimentation(self):
        print("Localidade: " , self.Ambiente.mapa[self.y][self.x])
        if self.Ambiente.mapa[self.y][self.x] == 1 or self.Ambiente.mapa[self.y][self.x] == 2:
            self.pontuacao += self.Clean(self.x,self.y)
            self.MovimentaLinha()
        else:
            self.MovimentaLinha()

    def executar(self):
        while self.Ambiente.objetosRestante > 0:
            clear = lambda: os.system('cls')
            clear()
            print("obj " , self.Ambiente.objetosRestante)
            print("SelfX = ", self.x)
            print("SelfY = ", self.y )
            self.Ambiente.renderizar('@','#','*', X_Agente = self.x, Y_Agente = self.y)
            self.RandomMovimentation()
            #input("Press Enter to continue...")
    
            
            
m1 = Mapa(m=20, n=20)
m1.generate(123)
#m1.renderizar('@','*')

r1 = ReativoBaseadoemModelo(m1)
r1.executar()
print("Pontuação Final: " , r1.pontuacao)
