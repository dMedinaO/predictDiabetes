'''
script que permite crear un directorio con el set de datos asociado, con el fin de poder ser utilizado para evaluar como predictor
'''

import pandas as pd
import sys
import os

#create elements to array
def parseArray(dataValues0, dataValues1, dataValues2, dataValues3, dataValues4, response, key):

    matrix = []
    for i in range(len(dataValues0)):

        if (key=='GG' or key == 'GI'):
            row = [dataValues0[i], dataValues1[i], dataValues2[i], dataValues3[i], dataValues4[i], "G"+str(response[i])]
        else:
            row = [dataValues0[i], dataValues1[i], dataValues2[i], dataValues3[i], dataValues4[i], response[i]]
        matrix.append(row)

    return matrix

dataSet = pd.read_csv(sys.argv[1])
output = sys.argv[2]

#manipulamos las columnas
keys = ['IB','I30','I60','I90','I120','GG','GI','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16']

#creamos los directorios y el set de datos
for i in range(5,len(keys)):

    command = "mkdir -p %s%s" % (output, keys[i])
    print command
    os.system(command)
    matrixData = parseArray(dataSet['IB'], dataSet['I30'], dataSet['I60'], dataSet['I90'], dataSet['I120'], dataSet[keys[i]], keys[i])

    header = ['IB','I30','I60','I90','I120', keys[i]]
    dataFrame = pd.DataFrame(matrixData, columns=header)
    nameExport = "%s%s/dataSet_%s.csv" % (output, keys[i], keys[i])
    dataFrame.to_csv(nameExport, index=False)
