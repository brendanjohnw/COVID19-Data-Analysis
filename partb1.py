## Part B Task 1

import re
import pandas as pd
import os 

# Getting the ID for each file and storing it into a Series
path = '/home/jovyan/assignment-1-brendanjohnw/cricket/'
file_name = []
file_ID = []

ID_pattern = '[A-Z]{4}\-[0-9]{3}[A-Z]?'
for file in os.listdir(path):
    path = '/home/jovyan/assignment-1-brendanjohnw/cricket/'
    if file.endswith(".txt"):
        file_path = path+file
        file_name.append(file)
        f = open(file_path,'r')
        text = f.read()
        file_ID.append(re.findall(ID_pattern,text)[0])
        
file_df = pd.DataFrame(list(zip(file_name,file_ID)), columns = ['filename','documentID'])
       
file_df.to_csv(r'partb1.csv',index = False)


        
        
        

            
        