import pickle
from jsonCompatibilityInProgress import *
from generators import *
from helperFunctions import *

def generate_secret_key(startSeed=None,output=dict(),outputTranspose=dict()):
    
    if startSeed is not None:
        secretKey = generate_small_randoms(startSeed)
    else:
        secretKey = generate_small_randoms()
    output['s'] = secretKey
    s_T = secretKey.transpose()
    output['s_T'] = s_T
    pickleString = pickle.dumps(output)
    with open("keyGenSecretData.pickle","wb") as f:
        f.write(pickleString)
    return secretKey

def generate_public_key(s,e,startSeed = None,output=dict()):
    
    A = generate_random_matrix22(startSeed)
    #e = generate_small_randoms(startSeed)
    
    t = A * s + e
    output['A'] = A
    output['t'] = t
    output['e'] = e
    outputA = matrixXbartoX(A) 
    print(type(outputA[0][0]))
    pickleString = pickle.dumps(output)
    with open("keyGenData.pickle","wb") as f:
        f.write(pickleString)
    return A, t

def keyGen(startSeed=None):

    secretKey = generate_small_randoms(startSeed)
    publicKey = generate_public_key(secretKey,startSeed)

    return publicKey,secretKey   




#TODO dat do funkcie enc


def encrypt(AMatrixpk1,tpk2,message,r,seed = None, outputU=dict(),outputV=dict(),outputDec=dict()):


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
    outputV['v'] = v
    outputU['u'] = u
    outputU['r'] = r
    outputV['r'] = r
    outputU['e1'] = e1
    outputU['v'] = v
    outputV['e2'] = e2
    outputU['A'] = A_t
    outputV['t'] = t_t
    outputU['m'] = message
    outputV['m'] = message
    outputDec['u'] = u
    outputDec['v'] = v
    pickleStringU = pickle.dumps(outputU)
    pickleStringV = pickle.dumps(outputV)
    pickleStringCip = pickle.dumps(outputDec)
    with open("encryptionUData.pickle","wb") as f:
        f.write(pickleStringU)
    with open("encryptionVData.pickle","wb") as f1:
        f1.write(pickleStringV)
    with open("CipherTextData.pickle","wb") as f2:
        f2.write(pickleStringCip)
    return u, v, e1, e2


def decrypt(uEnc,vEnc,sKey,output=dict(),outputSteps=dict()):
    
    m_n = vEnc - sKey.transpose() * uEnc
    m_nSplit = msgBitsToCoeffs(m_n)
    coefficients = decode(m_nSplit)
    m_nSplitDsc = compress(coefficients,ceil(qPolyMod/2))
    output = coeffsToMsg(m_nSplitDsc)
    outputSteps['m_n'] = m_n
    outputSteps['m_nSplit'] = m_nSplit
    outputSteps['coefficients'] = coefficients
    outputSteps['m_nSplitDsc'] = m_nSplitDsc
    outputSteps['result'] = coeffsToMsg(m_nSplitDsc)
    print("m_n =")
    print(m_n)
    print(coefficients)
    print(m_nSplitDsc)
    result = pickle.dumps(outputSteps)
    with open("result.pickle","wb") as f:
        f.write(result)
    return output

"""
#TEST
output = dict()
output['message'] = list()

resultArray = []
for j in range(1000):
    message = 'M'
    e = generate_keyGen_error()
    s1 = generate_secret_key()
    a,t = generate_public_key(s1,e)
    r = generate_small_randoms()
    u,v,e1,e2 = encrypt(a,t,poly_message(message),r,)
    decryptedMsg = decrypt(u,v,s1)
    resultArray.append(decryptedMsg['msg'])


print(resultArray.count('M'))
"""
