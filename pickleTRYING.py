import hashlib, time
from sage.all import *
import json

polyMod = 137
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


def msgXbarToX(message):
    messageList = message.coefficients()
    print(messageList)
    messageSplit = messageList[0]._polynomial
    print(messageSplit)
    return messageSplit


def smallRandomXbarToX(matrix):
    messageList = matrix.coefficients()
    messageSplit = []
    for i in range(2):
        row = []
        for j in range(1):
            index = i + j
            row.append(messageList[index]._polynomial)
        messageSplit.append(row)
    return messageSplit


def matrixXbartoX(matrix):
    messageList = matrix.coefficients()
    messageSplit = []
    for i in range(2):
        row = []
        for j in range(2):
            index = i*2 + j
            row.append(messageList[index]._polynomial)
        messageSplit.append(row)
    return messageSplit

def msgBitsToCoeffs(message):
    
    messageSplit = msgXbarToX(message)
    messageExp = messageSplit.exponents()
    print(messageExp)
    messageSplit = messageSplit.coefficients()
    print(messageSplit)
    arrayOfCoefficients = [0,0,0,0,0,0,0,0]
    i = 0
    for coe in range(ExpMod):
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
    for i in range(ExpMod):
        nextSeed = str(startSeed) + str(i)
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
    for i in range(ExpMod):
        nextSeed = str(startSeed) + str(i)
        hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
        bigRand = int.from_bytes(hash, 'big')
        rand = min + bigRand % (max - min + 1)
        coeffs1[i] = F(rand)
    return coeffs1

def generate_small_random_poly(startSeed=None,cbd = None):
    if startSeed is None:
        startSeed = str(time.time()) + '|'

    F = FiniteField(polyMod)
    R = PolynomialRing(F, 'x')
    x = R.gen()
    f = x**ExpMod + 1
    Rmodf = R.quotient(f)
    
    coeffs = PRF_small(startSeed,cbd)
    
    s = matrix([Rmodf(sum(coeffs[i]*x**i for i in range(ExpMod)))])
    
    return s




def generate_small_randoms(startSeed=None,cbd = None):

    F = FiniteField(polyMod)
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
    
    return s


def decompress(arr, q):

    decompressed_arr = [q * x for x in arr]
    return decompressed_arr

def compress(arr, q):

    compressd_arr = [x / q for x in arr]
    return compressd_arr

def generate_random_matrix22(startSeed = None):

    F = FiniteField(polyMod)
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
    print(A)
    return A


def generate_public_key(s,startSeed = None):
    
    A = generate_random_matrix22(startSeed)
    e = generate_small_randoms(startSeed)
    
    t = A * s + e
    
    return A, t

def keyGen(startSeed=None):

    secretKey = generate_small_randoms(startSeed)
    publicKey = generate_public_key(secretKey,startSeed)

    return publicKey,secretKey   

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


#TODO dat do funkcie enc


def encrypt(AMatrixpk1,tpk2,message,r,seed = None, output=dict()):


    e1 = generate_small_randoms(seed,2)
    e2 = generate_small_random_poly(seed,2)
    

    print("r = ")
    print(r)
    print("e1 = ")
    print(e1)
    print(smallRandomXbarToX(e1)[0])
    print(smallRandomXbarToX(e1)[1])
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


output = dict()
output['message'] = list()


m = poly_message("Z")


s1 = generate_small_randoms()

s2 = generate_small_randoms()

a,t = generate_public_key(s1)



aX = matrixXbartoX(a)
print(aX)
print(aX[0])
print(aX[1])

print(s1)
print(s2)
print("a =")
print(a)
print(str(a))
print(t)
r = generate_small_randoms()
charOutput, utest1, vtest1 = encrypt(a,t,m,r)

def enryptedOutputToJSON(charOutput):
    m_nSplitV = msgBitsToCoeffs(charOutput['v'])
    charOutput['v'] = [int(c) for c in m_nSplitV]

    m_nSplitU = msgBitsToCoeffs(charOutput['u'][0])
    m_nSplitU1 = msgBitsToCoeffs(charOutput['u'][1])
    charOutput['u'] = [[int(c) for c in m_nSplitU], [int(z) for z in m_nSplitU1]]

    output['message'].append(charOutput)

    jsonString = json.dumps(output)
    with open("data.json","w") as f:
        f.write(jsonString)
    return output

def JSONtoPolyEncryption(jsonOutput):
    u = jsonOutput['message'][0]['u']
    u = list_to_poly_matrix(u)
    u = u.transpose()
    print(u)
    v = jsonOutput['message'][0]['v']
    v = list_to_poly(v)
    print(v)
    return u,v


output = enryptedOutputToJSON(charOutput)
u,v = JSONtoPolyEncryption(output)

decryptedMsg = decrypt(u,v,s1)

jsonString1 = json.dumps(decryptedMsg)
with open("dataDec.json","w") as file:
    file.write(jsonString1)

print(decryptedMsg['msg'])

resultArray = []

for j in range(1000):
    newMessage = poly_message("Z")
    s1 = generate_small_randoms()
    r = generate_small_randoms()
    a,t = generate_public_key(s1)
    charOutput, utest1, vtest1 = encrypt(a,t,m,r)

    output = enryptedOutputToJSON(charOutput)
    u,v = JSONtoPolyEncryption(output)
    decryptedMsg = decrypt(u,v,s1)
    resultArray.append(decryptedMsg['msg'])


print(resultArray.count('Z'))