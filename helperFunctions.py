from compressAndDecode import *


def coeffsToMsg(decodedCoeffs,output = dict()):
    x = 0
    cnt = 0
    for coeffici in decodedCoeffs:
        if(coeffici == 1):
            x += 2**cnt
        cnt += 1
    output['msg'] = chr(x)
    return output

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

def list_to_poly(coefList):
    F = FiniteField(qPolyMod)
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
    F = FiniteField(qPolyMod)
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
    F = FiniteField(qPolyMod)
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
    numberF = ceil(qPolyMod/2)
    print(numberF)
    decompressedPoly = decompress(binary_array,numberF)
    m = matrix([Rmodf(sum(decompressedPoly[i]*x**(len(binary_array)-1-i) for i in range(len(binary_array))))])
    print(decompressedPoly)
    print(m)

    return m