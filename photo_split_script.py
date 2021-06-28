# Script que divide as fotografias organizadas em pastas pela sua idade e coloca-as em 5 classes.

import shutil
import os
    
source_dir = '/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/photos/{}'
target_dir = '/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/photos2/{}'

image_id = 0
for i in range(7, 100):
    this_src_dir = source_dir.format(str(i))
    this_dest_dir = ""
    if(i < 23):
        this_dest_dir = target_dir.format('young')
    elif(i < 35):
        this_dest_dir = target_dir.format('middle1')
    elif(i < 45):
        this_dest_dir = target_dir.format('middle2')
    elif(i < 60):
        this_dest_dir = target_dir.format('middle3')
    else:
        this_dest_dir = target_dir.format('old')

    file_names = os.listdir(this_src_dir)
    for file_name in file_names:
        if (os.path.getsize('/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/photos/'+ str(i) + "/" + file_name) > 334) & (file_name != '.DS_Store'):
            shutil.copy(os.path.join(this_src_dir, file_name), this_dest_dir)