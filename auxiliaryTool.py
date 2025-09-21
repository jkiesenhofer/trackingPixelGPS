import pandas as pd
import numpy as np
import requests
# Reading a XML file into a DataFrame
df = pd.read_csv('SAPrules.xml')

array = df.values.tolist() # xml-list
lines=1236
b=array[0:lines]

#print(b[10:20])
n=df.to_string()
#print(n)

for i in range(lines):
    a=str(b[i]).split('<transaction>')[0]
    #print(str(i)+a)
    
#print(len(array))
m=85
#print(type(array))

for j in range(m):

    u = list(n.split('<transaction>')[j])
    uu = list(n.split('<transaction>')[1:m])

#print(u[0:(20)])

    k="".join(str(x) for x in u[0:(20)])

    print(k.split('<')[0])
