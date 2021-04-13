
## Part B Task 4
import re
import pandas as pd
import os
import sys
from nltk.stem.porter import*



def preprocessing(text):
    extract_except = '[^A-Za-z ]+'
    text = re.sub(extract_except," ",text)
    text = (text.lower()).replace('\t\n'," ") 
    return text
    

keyword_list = []
ID_doc = pd.read_csv("partb1.csv", encoding = 'UTF-8')
if __name__ == "__main__":
    
    for i, arg in enumerate(sys.argv):
        keyword_list.append(arg)
 
keyword_list = keyword_list[1:]

path = '/home/jovyan/assignment-1-brendanjohnw/cricket/'
match_files = []
match_ID = []
stemmer_base_words = []
porter_stemmer = PorterStemmer()
file_ID_dict = ID_doc.set_index('filename')['documentID'].to_dict()

for file,ID in zip(file_ID_dict.keys(),file_ID_dict.values()):
    all_match = True
    #print(file,ID)   
    if file.endswith(".txt"):
        file_path = path+file
        f = open(file_path,'r')
        text = f.read()
        f.close()
        processed_text = preprocessing(text)
        #print(processed_text)
        for word in keyword_list:
            wordpat = porter_stemmer.stem(word)
            pattern = "\\b"+wordpat
            #print(pattern)
            match = re.search(pattern,processed_text)
            if match:
                next
            else:
                all_match = False
                break
    if all_match is True:
        match_ID.append(ID)

if match_ID:
    print("The following documents matched your keywords:")
    for ID in match_ID:
        print(ID)
        i = i+1
else:
    print("There were no documents with the following keywords:")
    
    for word in keyword_list:
        print(word)
        


