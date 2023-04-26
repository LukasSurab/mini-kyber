import json
from helperFunctions import *

def enryptedOutputToJSON(charOutput,output = dict()):
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