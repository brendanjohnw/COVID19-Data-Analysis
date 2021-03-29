  ## Part B Task 5
import re
import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.porter import*
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from numpy import dot
from numpy.linalg import norm
import math

# comment out if not downloaded

#nltk.download('punkt')
#nltk.download('stopwords')
# from week 3 example

'''Data Cleaning steps:
- Remove Spaces
- Remove Punctuation
- Case Normalization
- Tokenize
- Get rid of Stop words
- Lemmatize
- Porter Stem

TF-IDF steps
- get the term frequency for each document
- place in a dictionary
- find the inverse document frequency
- place in a dictionary
- calculate TF-IDF score for each word
- place in a dictionary
- find keyword matches in the dictionary and print out ID for the 
'''
porter_stemmer = PorterStemmer()
## Data Cleaning

        
''' What we have: '''
def prepreprocessing(text):
    extract_except = '[^A-Za-z ]+'
    text = re.sub(extract_except," ",text)
    text = (text.lower()).replace('\t\n'," ")
    return text
def preprocessing(text):
    extract_except = '[^A-Za-z ]+'
    text = re.sub(extract_except," ",text)
    text = (text.lower()).replace('\t\n'," ") 
    # tokenizing
    token_text = [word for word in word_tokenize(text) if not word in stopwords.words()]
    #removing stop words             
    return token_text
    
def stemmed_keywords(keywords):
    porter_stemmer = PorterStemmer()
    stemmed_keyword_list = []
    for word in keywords:
        word = porter_stemmer.stem(word)
        stemmed_keyword_list.append(word)
    return stemmed_keyword_list
    
def stem_document_words(tokened_text):
    porter_stemmer = PorterStemmer()
    stemmed_words = []
    for word in tokened_text:
        stem_word = porter_stemmer.stem(word)
        stemmed_words.append(stem_word)
    return stemmed_words
    
def get_word_freq(word_list):
    word_freq_dict ={}
    for word in word_list:
        if word not in word_freq_dict:
            word_freq_dict[word]=1
        elif word in word_freq_dict:
            word_freq_dict[word]+=1
    return word_freq_dict

def get_term_freq_keywords(keyword_list,key_dict):
    for word in keyword_list:
        if word in key_dict:
            key_dict[word]+=1
    return key_dict

def cosine_sim(v1, v2):
    return dot(v1, v2)/(norm(v1)*norm(v2))

keyword_list = []
ID_doc = pd.read_csv("partb1.csv", encoding = 'UTF-8')
if __name__ == "__main__":
    
    for i, arg in enumerate(sys.argv):
        keyword_list.append(arg)

keyword_list = keyword_list[1:]
keyword_list = stemmed_keywords(keyword_list)
path = '/home/jovyan/assignment-1-brendanjohnw/cricket/'
match_files = []
match_ID = []

porter_stemmer = PorterStemmer()
file_ID_dict = ID_doc.set_index('filename')['documentID'].to_dict()
doc_dic = {}
key_dic = {}
ID_sim_dic = {}


for file,ID in zip(file_ID_dict.keys(),file_ID_dict.values()):
    all_match = True
    if file.endswith(".txt"):
        
        file_path = path+file
        f = open(file_path,'r')
        text = f.read()
        f.close()
        processed_text = prepreprocessing(text)
        # keyword list is a vector of stemmed keywords entered by the user
        
        # tokenized_text is a list of words in the file without stopwords or punctuations
        for word in keyword_list:
            pattern = "\\b"+word
            match = re.search(pattern,processed_text)
            if match:
                next
            else:
                all_match = False
                break
    if all_match is True:
        tokenized_text= preprocessing(text)
        match_ID.append(ID)
        #stemmed_tok_text is the vector of stemmed words from the matched text
        # print(tokenized_text)
        stemmed_tok_text = stem_document_words(tokenized_text)
        #doc_dic stores the term frequency(t_f) of the words into a dictionary in the matched document
        doc_dic = get_word_freq(stemmed_tok_text)
        key_dic = get_term_freq_keywords(keyword_list,dict.fromkeys(doc_dic,0))
        # term_counts contain the term frequencies for the keyword vector and the matched document vector
        terms = list(doc_dic.keys())
        term_counts = [list(doc_dic.values()),list(key_dic.values())]
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(term_counts)
        doc_tfidf = tfidf.toarray()
        #unit_vector
        unit_vec = [x/(math.sqrt(3)) for x in list(key_dic.values())]
        sims = [cosine_sim(unit_vec, doc_tfidf[d_id]) for d_id in range(doc_tfidf.shape[0])]
        ID_sim_dic[ID]=round(sims[0],4)
        print(sims)
        
        


if match_ID:
    print("The following documents matched your keywords:")
    for ID in match_ID:
        print(ID)
        i = i+1
    ID_sim_dic = dict(sorted(ID_sim_dic.items(), key = lambda item: item[1],reverse = True))
    ID_sort = list(ID_sim_dic.keys())
    sim_sort = list(ID_sim_dic.values())
    print("\ndocumentID score")
    for i in range(len(ID_sort)):
        print(ID_sort[i],sim_sort[i])
    
else:
    print("There were no documents with the following keywords:")
    
    for word in keyword_list:
        print(word)

