from PRF import *

def decode(coeffsMsg):
    coefficients = []
    for coeffic in coeffsMsg:
        if math.isclose(ceil(qPolyMod/2),coeffic,abs_tol=ceil(qPolyMod/2)/2):
            coeffic = ceil(qPolyMod/2)
        else:
            coeffic = 0
        coefficients.append(coeffic)
    print("decoded:")    
    print(coefficients)    
    return coefficients

def decompress(arr, q):

    decompressed_arr = [q * x for x in arr]
    print("decompressed:") 
    return decompressed_arr

def compress(arr, q):

    compressd_arr = [x / q for x in arr]
    print("compressed:")
    print(compressd_arr)
    return compressd_arr
