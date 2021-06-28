# Script para dividir as fotografias entre treino e teste.

import shutil
import os
import glob
    
for i in glob.glob("/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/photos2/*"):
    filename = i.split("/")[-1]
    if not os.path.exists("/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/train/"+filename+"/"):
        os.makedirs("/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/train/"+filename+"/")
        os.makedirs("/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/test/"+filename+"/")

    cont = 1
    for i in glob.glob(i+"/*"):
        if cont < 5760: # 90% para treino
            shutil.copy(i,"/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/train/"+filename+"/")
        elif cont < 6400: # 10% para treino
            shutil.copy(i,"/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/test/"+filename+"/")
        else:
            break
        cont+=1
