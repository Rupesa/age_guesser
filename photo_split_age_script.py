# Script que divide as fotografias e coloca-as em pastas pela sua idade.

import os
import glob
import shutil

sefw = True
for i in glob.glob("/Users/ruisantos/Desktop/ano4/aa/project2/wiki_crop/*/*.jpg"):
    filename = i.split("/")[-1]
    year1 = (int) (filename.split("_")[1].split("-")[0])
    year2 = (int) (filename.split("_")[-1].split(".jpg")[0])
    age = year2 - year1
    if not os.path.exists("/Users/ruisantos/Desktop/ano4/aa/project2/wiki_crop/photos/"+str(age)+"/"):
        os.makedirs("/Users/ruisantos/Desktop/ano4/aa/project2/wiki_crop/photos/"+str(age)+"/")
    shutil.move(i,"/Users/ruisantos/Desktop/ano4/aa/project2/wiki_crop/photos/"+str(age)+"/"+filename)