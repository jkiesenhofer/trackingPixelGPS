import pandas as pd
import ipaddress as ip

df = pd.read_csv('IParray.csv')
array = df.values.tolist()
a0=list(str(['104.18::183.229']).split("::")[1])

b=array[0:(30)][:]
#b=df.to_string()
print(a0)

for k in range(0,2):
    b=str(a0[k]).split("s")[0]
    a0[k]=list("".join(b))
    #c=int(ip.IPv4Address(a0[k]))
    print(a0)
q = lambda a:a+1

print(q)
