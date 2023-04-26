import hashlib, time
from sage.all import *

qPolyMod = 137
ExpMod = 8

def PRF_small(startSeed = None,cbd = None):
    F = FiniteField(qPolyMod)
    if startSeed is None:
        startSeed = str(time.time()) + '|'
    min = -1
    max = 1
    if cbd is not None:
        min = -2
        max = 2
    coeffs1 = [0,0,0,0,0,0,0,0]
    for i in range(ExpMod):
        nextSeed = str(startSeed) + str(i)
        hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
        bigRand = int.from_bytes(hash, 'big')
        rand = min + bigRand % (max - min + 1)
        coeffs1[i] = F(rand)
    return coeffs1


def PRF(startSeed = None):
    F = FiniteField(qPolyMod)
    if startSeed is None:
        startSeed = str(time.time()) + '|'
    min = 0
    max = 232
    coeffs1 = [0,0,0,0,0,0,0,0]
    for i in range(ExpMod):
        nextSeed = str(startSeed) + str(i)
        hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
        bigRand = int.from_bytes(hash, 'big')
        rand = min + bigRand % (max - min + 1)
        coeffs1[i] = F(rand)
    return coeffs1