import pandas as pd
import ipaddress as ip

df = pd.read_csv('IParray.csv')
array = df.values.tolist()

a0=str(['104.18.187.229']).split("'")[1]

a=array[0:(30)][:]
print(a0)

for k in range(0,len(a)):
    b=str(a[k]).split("'")[1]
    a[k]=b
    c=int(ip.IPv4Address(a[k]))
    print(b)
q = lambda a:a+1

print(q)
