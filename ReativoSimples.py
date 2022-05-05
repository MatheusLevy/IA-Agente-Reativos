from enum import Enum
import os
import random
from Mapa import Mapa
import time
import numpy as np

#Enum dos movimentos possiveis pra o Agente
class Movimento(Enum):
    Cima  = 1
    Baixo = 2
    Esquerda = 3
    Direita = 4
      
class ReativoSimples:
    
    #@Parametros:
    #RandomMov: True ou False Para definir movimentação Aleatório ou Linha a Linha
    def __init__(self, Mapa, randomMov= True):      
        self.Movimentacao = randomMov
        self.x = 0
        self.y = 0
        self.sentido = "direita" # Sentido pode ser esquerda ou direita Utilizado para movimentação Linha  a Linha
        self.Ambiente = Mapa     # Recebe o mapa
        self.pontuacao = 0       # Conta a pontuação do Agente 


    #Função que pega um objeto no qual o agente esta em cima
    def Clean(self, x, y):
        if self.Ambiente.mapa[y][x] == 1:           # Verifica se na posição existe um objeto de valor 1.
            pontos = 10                             # Se sim, incrementa a pontuação
        elif self.Ambiente.mapa[y][x] == 2:         # O mesmo para objetos de valor 2
            pontos = 20
        self.Ambiente.mapa[y][x] = 0                # Limpa o valor da localização colocando 0 no lugar
        self.Ambiente.objetosRestante -= 1          # Decrementa os objetos restantes do mapa
        return pontos   

    #Define o movimento de subir
    def Cima(self):
        if self.y - 1 >= 0: #Verifica se não irá sair para fora do mapa
            self.y -= 1     
    #Define o movimento de descer
    def Baixo(self):
        if self.y + 1 < self.Ambiente.m : # Verifica se irá sair para fora do mapa
            self.y += 1
    #Define o movimento de ir para Esquerda
    def Esquerda(self):
        if self.x - 1 >= 0:
            self.x -= 1
    def Direita(self):
        if self.x + 1 < self.Ambiente.n:
            self.x += 1

    #Define o movimento Aleatório
    def MovimentaRandom(self):
        mv = random.choice(list(Movimento)) # Pega um movimento aleatório
        print(mv)
        if mv == Movimento.Cima:
            self.Cima()
        elif mv == Movimento.Baixo:
            self.Baixo()
        elif mv == Movimento.Esquerda:
            self.Esquerda()
        elif mv == Movimento.Direita:
            self.Direita()
    
    # Define o movimento em linha:
    def MovimentaLinha(self):
        if self.sentido == "direita":
            if (self.x + 1 < self.Ambiente.n): #Verifica se não esta no final da linha a direita
                self.Direita()
            else:                              #Se estiver no final da linha
                self.Baixo()                   #Vai para baixo e agora percorre da direita para esquerda
                self.sentido = "esquerda"

        elif self.sentido == "esquerda":
            if(self.x -1 >= 0):                # Verifica se não esta no final da linha a esquerda
                self.Esquerda()                
            else:
               if(self.y + 1 < self.Ambiente.m):
                    self.Baixo()               
                    self.sentido = "direita"

    #Verifica se exite um objeto na localização atual do agente
    # @Parametros:
    # LestadeObjetosPossiveis: Lista de valores de objetos no mapa neste caso [1,2] 
    def VerficaObjeto(self, ListadeObejetosPossiveis):
        for objeto in ListadeObejetosPossiveis:
            if self.Ambiente.mapa[self.y][self.x] == objeto:
                return True
        return False
    
    #Define a movimentação do agente
    def Movimenta(self):
        if self.VerficaObjeto([1,2]): #Verifica se existe um objeto na localização atual
            self.pontuacao += self.Clean(self.x,self.y) #Retira o objeto e incrementa a pontuação
        else:
            if self.Movimentacao: 
                self.MovimentaRandom()
            else:
                self.MovimentaLinha()

    
    def executar(self):
        while self.Ambiente.objetosRestante > 0:
            clear = lambda: os.system('cls')
            clear()
            print("obj " , self.Ambiente.objetosRestante)
            print("SelfX = ", self.x)
            print("SelfY = ", self.y )
            self.Ambiente.renderizar('@','#',' ', X_Agente = self.x, Y_Agente = self.y)
            self.Movimenta() 

Tempos = []
for _ in range(5):   
    m1 = Mapa(m=20, n=20)
    m1.generate(123456)
    inicio = time.process_time()
    r1 = ReativoSimples(m1, randomMov= True)
    r1.executar()
    fim = time.process_time()
    Tempos.append(fim-inicio)

Tempos = np.array(Tempos)

clear = lambda: os.system('cls')
clear()

print("Tempos: ", Tempos)
print("Media: ", np.mean(Tempos), "s(+-) ", np.std(Tempos))


#print("Pontuação Final: " , r1.pontuacao)
