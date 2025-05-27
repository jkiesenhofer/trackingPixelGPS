import pandas as pd
import numpy as np
import requests
# Reading a CSV file into a DataFrame
df = pd.read_csv('IParray.csv')
array = df.values.tolist()
b=array[0:29]
X=np.arange(0, 30, 1)
def get_geocoordinates(ip_adresse):
    url = f"http://ip-api.com/json/{ip_adresse}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        return data["lat"], data["lon"]
    else:
        return None
ip_adresse1 = "213.162.73.172"  # Beispiel-IP-Adresse Vienna, Austria
geokoordinaten1 = get_geocoordinates(ip_adresse1)
print('213.162.73.172', 0, geokoordinaten1)
for i in range(0, 1):
    a=str(b[i]).split("'")[1]
    b=get_geocoordinates(a)
    c=X[i]
    print(a,X[i]+1,b)
    #print(X[i]+1)
for i in range(0, len(X)):
    k='geokoordinaten'+str(i)
    n='ip_adresse'+str(i)
    #print(X[i],k,n)
    k = get_geocoordinates(n)
    d=X[i]
    #print(d)