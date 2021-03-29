# Part B Task 2
import re
import os
import sys

if __name__ == "__main__":
    for i,arg in enumerate(sys.argv):
        file_arg = arg
path = '/home/jovyan/assignment-1-brendanjohnw/cricket/'
extract_except = '[^A-Za-z ]+'

for file in os.listdir(path):   
    if file.endswith(".txt"):
        file_path = path+file
        f = open(file_path,'r')
        text = f.read()
        text = re.sub(extract_except," ",text)
        text = (text.lower()).replace('\t\n'," ") 
        filename = 'cricket'+ file
        if filename == file_arg:
            print(text)
        with open(filename,'w') as f:
            f.write(text)
        
            
        
            
        
        

    
