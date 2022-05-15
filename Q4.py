import numpy as np     
li=[]
import csv
with open("Q4dataset.csv",'r') as r:
    read=csv.reader(r)
    li=list(read)
    li.sort(key=lambda x: x[2])
food = np.array(li) 
print(food) 
