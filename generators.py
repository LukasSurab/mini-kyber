import time
from sage.all import *
from PRF import *

def generate_random_matrix22(startSeed = None):

    F = FiniteField(qPolyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    if startSeed is None:
        startSeed = str(time.time()) + '|'
        coeffs1 = PRF(startSeed)
        coeffs2 = PRF(startSeed+str(1))
        coeffs3 = PRF(startSeed+str(2))
        coeffs4 = PRF(startSeed+str(3))
    else:
        coeffs1 = PRF(startSeed)
        coeffs2 = PRF(startSeed+1)
        coeffs3 = PRF(startSeed+2)
        coeffs4 = PRF(startSeed+3)

    A = matrix([[Rmodf(sum(coeffs1[i]*x**i for i in range(ExpMod))),Rmodf(sum(coeffs2[i]*x**i for i in range(ExpMod)))], 
                [Rmodf(sum(coeffs3[i]*x**i for i in range(ExpMod))),Rmodf(sum(coeffs4[i]*x**i for i in range(ExpMod)))]])
    print("A:") 
    return A


def generate_small_randoms(startSeed=None,cbd = None):

    F = FiniteField(qPolyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    
    if startSeed is None:
        startSeed = str(time.time()) + '|'
        coeffs1 = PRF_small(startSeed,cbd)
        coeffs2 = PRF_small(startSeed+str(1),cbd)
    else:
        coeffs1 = PRF_small(startSeed,cbd)
        coeffs2 = PRF_small(startSeed+1,cbd)
    
    s = matrix([[Rmodf(sum(coeffs1[i]*x**i for i in range(ExpMod)))], [Rmodf(sum(coeffs2[i]*x**i for i in range(ExpMod)))]])
    print("generated value:") 
    print(s)
    return s


def generate_small_random_poly(startSeed=None,cbd = None):
    if startSeed is None:
        startSeed = str(time.time()) + '|'

    F = FiniteField(qPolyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    
    coeffs = PRF_small(startSeed,cbd)
    
    s = matrix([Rmodf(sum(coeffs[i]*x**i for i in range(ExpMod)))])
    print("s:") 
    print(s)
    return s

def generate_keyGen_error(startSeed=None):
    
    if startSeed is not None:
        keyGenError = generate_small_randoms(startSeed + 150)
    else:
        keyGenError = generate_small_randoms()
    return keyGenError
