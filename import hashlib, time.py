import hashlib, time
from sage.all import *
from random import seed as set_random_seed
import json

polyMod = 233
ExpMod = 8

def coeffsToMsg(decodedCoeffs):
    x = 0
    cnt = 0
    for coeffici in decodedCoeffs:
        if(coeffici == 1):
            x += 2**cnt
        cnt += 1
    output['msg'] = chr(x)
    return output

def decode(coeffsMsg):
    coefficients = []
    for coeffic in coeffsMsg:
        if math.isclose(ceil(polyMod/2),coeffic,abs_tol=ceil(polyMod/2)/2):
            coeffic = ceil(polyMod/2)
        else:
            coeffic = 0
        coefficients.append(coeffic)
    return coefficients

def msgBitsToCoeffs(message):
    
    messageList = message.coefficients()
    print(messageList)
    messageSplit = messageList[0]._polynomial
    print(messageSplit)
    messageExp = messageSplit.exponents()
    print(messageExp)
    messageSplit = messageSplit.coefficients()
    print(messageSplit)
    arrayOfCoefficients = [0,0,0,0,0,0,0,0]
    i = 0
    for coe in range(8):
        if coe in messageExp:
            arrayOfCoefficients[coe] = messageSplit[i]
            i += 1 
    return arrayOfCoefficients

def PRF_small(startSeed = None,cbd = None):
    F = FiniteField(polyMod)
    if startSeed is None:
        startSeed = str(time.time()) + '|'
    min = -1
    max = 1
    if cbd is not None:
        min = -2
        max = 2
    coeffs1 = [0,0,0,0,0,0,0,0]
    for i in range(8):
        nextSeed = startSeed + str(i)
        hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
        bigRand = int.from_bytes(hash, 'big')
        rand = min + bigRand % (max - min + 1)
        coeffs1[i] = F(rand)
    return coeffs1


def PRF(startSeed = None):
    F = FiniteField(polyMod)
    if startSeed is None:
        startSeed = str(time.time()) + '|'
    min = 0
    max = 232
    coeffs1 = [0,0,0,0,0,0,0,0]
    for i in range(8):
        nextSeed = startSeed + str(i)
        hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
        bigRand = int.from_bytes(hash, 'big')
        rand = min + bigRand % (max - min + 1)
        coeffs1[i] = F(rand)
    return coeffs1

def generate_small_random_poly(seed=None):
    if seed is not None:
        set_random_seed(seed)

    #TODO setting 
    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    
    coeffs = PRF_small()
    
    s = matrix([Rmodf(sum(coeffs[i]*x**i for i in range(8)))])
    
    return s




def generate_small_randoms(seed=None):
    if seed is not None:
        set_random_seed(seed)

    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)

    coeffs1 = PRF_small()
    coeffs2 = PRF_small()
    
    s = matrix([[Rmodf(sum(coeffs1[i]*x**i for i in range(8)))], [Rmodf(sum(coeffs2[i]*x**i for i in range(8)))]])
    
    return s


def decompress(arr, q):

    decompressed_arr = [q * x for x in arr]
    return decompressed_arr

def compress(arr, q):

    compressd_arr = [x / q for x in arr]
    return compressd_arr

def generate_random_matrix22(seed = None,):
    if seed is not None:
        set_random_seed(seed)

    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)

    coeffs1 = PRF()
    coeffs2 = PRF()
    coeffs3 = PRF()
    coeffs4 = PRF()
    
    A = matrix([[Rmodf(sum(coeffs1[i]*x**i for i in range(8))),Rmodf(sum(coeffs2[i]*x**i for i in range(8)))], 
                [Rmodf(sum(coeffs3[i]*x**i for i in range(8))),Rmodf(sum(coeffs4[i]*x**i for i in range(8)))]])
    print(A)
    return A

# def generate_public_key():
    
    
#     A = generate_random_matrix22(seed = None)

#     s = generate_small_randoms(seed = None)
#     e = generate_small_randoms(seed = None)
    
    

#     t = A * s + e
#     return A, t

def generate_public_key(s):
    
    A = generate_random_matrix22(seed=None)
    e = generate_small_randoms(seed=None)
    
    t = A * s + e
    
    return A, t

s = generate_small_randoms(seed = None)
print(s)

def keyGen(seed=None):

    secretKey = generate_small_randoms(seed)
    publicKey = generate_public_key(secretKey)

    return publicKey,secretKey

pubKey, secKey = keyGen(110)
print("PK A ==")
print(pubKey[0])
print("PK t ==")
print(pubKey[1])
print("SK ==")
print(secKey)

A1, t1 = generate_public_key(s)
A2, t2 = generate_public_key(s)

print("A1 =\n{}\nt1 =\n{}\n".format(A1, t1))
print("A2 =\n{}\nt2 =\n{}\n".format(A2, t2))

class SecretKey:
    def __init__(self, seed=None):
        self.F = FiniteField(polyMod)
        self.R = PolynomialRing(self.F, 'x')
        self.x = self.R.gen()
        self.f = self.x**ExpMod + 1
        self.Rmodf = self.R.quotient(self.f)
        self.seed = seed

    def generate_key(self):
        
        sk = generate_small_randoms(seed = None)
        
        return sk
    
    
class PublicKey:
    def __init__(self, seed=None):
        self.F = FiniteField(polyMod)
        self.R = PolynomialRing(self.F, 'x')
        self.x = self.R.gen()
        self.f = self.x**ExpMod + 1
        self.Rmodf = self.R.quotient(self.f)
        self.seed = seed
        self.a = None
        self.t = None
        
    def generate_key(self, s):
        self.a, self.t = generate_public_key(s)
        
        return self.a, self.t
        
    def update_key(self, new_seed):
        self.seed = new_seed
        self.generate_key(self.seed)

def list_to_poly(coefList):
    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x') 
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    Coefficients = []
    for coeffic in coefList:
        Coefficients.insert(0,coeffic)
    messagePoly = matrix([Rmodf(sum(Coefficients[i]*x**(len(Coefficients)-1-i) for i in range(len(Coefficients))))])

    return messagePoly

def list_to_poly_matrix(coefList):
    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x') 
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    Coefficients = []
    for coeffic in coefList[0]:
        Coefficients.insert(0,coeffic)
    Coefficients1 = []
    for coeffici in coefList[1]:
        Coefficients1.insert(0,coeffici)
    messagePoly = matrix([Rmodf(sum(Coefficients[i]*x**(len(Coefficients)-1-i) for i in range(len(Coefficients)))),Rmodf(sum(Coefficients1[i]*x**(len(Coefficients1)-1-i) for i in range(len(Coefficients1))))])

    return messagePoly            
        
# TODO Dat do funkcie
def poly_message(message):

    print(message)
    if isinstance(message,str):
        message = ord(message)
    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x') 
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    binary_string = bin(message)[2:]   
    binary_array = [int(bit) for bit in binary_string]   # convert string to array of integers

    print(binary_array)   
    print(len(binary_array))
    messagePoly = [Rmodf(sum(binary_array[i]*x**(len(binary_array)-1-i) for i in range(len(binary_array))))]
    print(messagePoly)
    numberF = ceil(polyMod/2)
    print(numberF)
    decompressedPoly = decompress(binary_array,numberF)
    m = matrix([Rmodf(sum(decompressedPoly[i]*x**(len(binary_array)-1-i) for i in range(len(binary_array))))])
    print(decompressedPoly)
    print(m)

    return m

m = poly_message("Z")

sk1 = SecretKey(seed=42)
s1 = sk1.generate_key()

sk2 = SecretKey(seed=123)
s2 = sk2.generate_key()

pk = PublicKey(seed = None)
a, t = pk.generate_key(s1)

print(s1)
print(s2)
print("a =")
print(a)
print(str(a))
print(t)

#TODO dat do funkcie enc


def encrypt(AMatrixpk1,tpk2,message,r,seed = None, output=dict()):


    e1 = generate_small_randoms(seed)
    e2 = generate_small_random_poly(seed)

    print("r = ")
    print(r)
    print("e1 = ")
    print(e1)
    print("e2 = ")
    print(e2)

    A_t = AMatrixpk1.transpose()
    u = A_t * r + e1
    print("u =")
    print(u)
    t_t = tpk2.transpose()
    v = t_t * r + e2 + message
    print("v =")
    print(v)
    output['v'] = v
    output['u'] = u
    return output, u, v

output = dict()
output['message'] = list()

r = generate_small_randoms(None)
charOutput, utest1, vtest1 = encrypt(a,t,m,r,11)


m_nList = charOutput['v'].coefficients()
m_nSplit = m_nList[0]._polynomial
m_nSplit = m_nSplit.coefficients()
charOutput['v'] = [int(c) for c in m_nSplit]

m_nList = charOutput['u'].coefficients()
m_nSplit = m_nList[0]._polynomial
m_nSplit = m_nSplit.coefficients()
m_nSplit1 = m_nList[1]._polynomial
m_nSplit1 = m_nSplit1.coefficients()
charOutput['u'] = [[int(c) for c in m_nSplit], [int(z) for z in m_nSplit1]]

output['message'].append(charOutput)

jsonString = json.dumps(output)
with open("data.json","w") as f:
    f.write(jsonString)

u = output['message'][0]['u']
u = list_to_poly_matrix(u)
u = u.transpose()
print(u)
v = output['message'][0]['v']
v = list_to_poly(v)
print(v)

def decrypt(uEnc,vEnc,sKey,output=dict()):
    
    m_n = vEnc - sKey.transpose() * uEnc
    m_nSplit = msgBitsToCoeffs(m_n)
    coefficients = decode(m_nSplit)
    m_nSplitDsc = compress(coefficients,ceil(polyMod/2))
    output = coeffsToMsg(m_nSplitDsc)
    print("m_n =")
    print(m_n)
    print(coefficients)
    print(m_nSplitDsc)
    return output

decryptedMsg = decrypt(utest1,vtest1,s1)

jsonString1 = json.dumps(decryptedMsg)
with open("dataDec.json","w") as file:
    file.write(jsonString1)

print(decryptedMsg['msg'])
