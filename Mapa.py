from utils import *

class Mapa:
    
    def __init__(self, m=20, n=20, objetos=10):
        self.m = m
        self.n = n 
        self.objetos = objetos
        self.objetosRestante = objetos
        self.mapa = np.zeros((m,n), dtype= np.int8)    
    
    def generate(self, seedA):
        seed(seedA)
        if(self.objetos > (self.n+1) * (self.m+1)):
            print("Erro: Número de Objetos maior do que o Mapa!")
            return 0
        
        Pontos = geradordeCoordenadasXY(self.objetos, self.n-1, self.m-1)
        print(Pontos)
        input("Press Enter to continue...")
        for ponto in Pontos:
            random_m, random_n = ponto
            self.mapa[random_m][random_n] = 1

                


    def toString(self, CaracterObjeto, CaracterVazio):
        stringMapa = np.empty((self.m, self.n), dtype=object) #Criar a Matriz de Strings vazia
        for i in range(self.m):
            for j in range(self.n):
                if self.mapa[i][j] == 1:                       #Onde tiver 1 vira o caractere de Objeto
                    stringMapa[i][j] = CaracterObjeto   
                else:
                    stringMapa[i][j] = CaracterVazio           #Onde tiver 0 vira caractere de Vazio
        return stringMapa

    def renderizar(self, CaracterObjeto, CaracterVazio, X_Agente=0, Y_Agente=0 ):
        render = self.toString(CaracterObjeto, CaracterVazio)
        render[Y_Agente][X_Agente] = 'A'
        for line in render:
            print ('  '.join(map(str, line)))
        print("x: " , X_Agente)
        print("y: " , Y_Agente)
        

