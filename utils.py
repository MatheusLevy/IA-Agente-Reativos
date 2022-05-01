from random import random, seed
from random import randint
import string
from time import sleep
import numpy as np
import os

def geradordeCoordenadasXY(quantidade, maxN, maxM):
    Pontos = []
    while len(Pontos) < quantidade:
        random_n = randint(0, maxN)
        random_m = randint(0, maxM)
        if (random_n, random_m) not in Pontos:
            Pontos.append((random_n, random_m))
    return Pontos

