import sys
import pandas as pd
import os
from pathlib import Path

# import csv 



def combine(files):
    
    #Check if  files exist
    if not len(files):

        return None
      
    for i in range(len(files)):
     
        
        _, ext = os.path.splitext(files[i])

     

        """Check if its .csv""" 
        if ext!= '.csv':
            # raise TypeError
            raise Exception('File extension is not correct')
            # print('File extension incorrect')
            # return False
        """Check if the path is correct""" 
        p = Path(files[i])

        if not p.exists():
            raise IOError('File does not exist')
            # print('File does not exist')
            # return False


    for i in range(len(files)):
        # if i==0:
        #     print('email_hash,category,filename') 
              
        """splitting path to obtain file name"""
        file_name = files[i].split('/')[-1]
        """Creating chunks to reduce storage""" 
        for chunks in pd.read_csv(files[i], chunksize=10e5):
            
            chunks['filename'] = file_name
            if i==0:
                print(','.join(chunks.columns))
            print(chunks.to_csv(header=False, index=False,chunksize=10e5))




"""Main Function"""
if __name__ == '__main__':
   
    combine(sys.argv[1:])
