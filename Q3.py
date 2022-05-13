import csv
import re
from collections import defaultdict

text="Python has tools for almost every aspect of scientific computing. The Bank of America uses Python to crunch its financial data and Facebook looks upon the Python library Pandas for its data analysis. While there are many libraries available to perform data analysis in Python, here are a few: NumPy, SciPy, Pandas and Matplotlib."
shortword=re.compile(r'\W*\b\w{1,5}\b')
newtext=shortword.sub('',text)

writer = csv.writer(open("output.txt", 'w' ), delimiter=';')
with open('about.txt.txt','a') as r: 
    writer=csv.writer(r)
    writer.writerow([])
    writer.writerow(["Words with atleast 6 letters:"])
    writer.writerow([newtext])

textlist=text.split() 
temp=defaultdict(int)
for j in textlist:
    for i in j.split():
        temp[j] += 1
fre=max(temp,key=temp.get)
with open('about.txt.csv','a') as f: 
    writer=csv.writer(f)
    writer.writerow(["Most frequently used word:"])
    writer.writerow([str(fre)])
 
#printing file
with open('about.txt.csv','r') as a:
    contents=a.read()
    print(contents)
