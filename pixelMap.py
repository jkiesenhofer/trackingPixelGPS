import pandas as pd
import numpy as np
import requests
# Reading a CSV file into a DataFrame
df = pd.read_csv('IParray.csv')
array = df.values.tolist()
lines=6
b=array[0:(lines+1)]
X=np.arange(0, lines, 1)
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
for i in range(0, lines+1):
    a=str(b[i]).split("'")[1]
    b[i]=a
b=(['213.162.73.172']+b[0:lines])*5
cities=['Vienna', 'Dusseldorf', 'Milan','Linz', 'Bothell','Mandaluyong City','Bothell']*5
IDs=[13.6500, 51.2215, 9.1885, -122.2054, -122.2054, 121.0410, -122.2054]*5
#for i in range(0,len(IDs)):
IDs[0]=48.0167
pixel=[13.6500, 51.2215, 9.1885, -122.2054, -122.2054, 121.0410, -122.2054]*5
for i in range(0,len(pixel)):
    #pixel[i]='47.0257'
    pixel[i]=get_geocoordinates(b[i])[1]
df = pd.DataFrame({"IPV4": b,
                   "City": cities,
                   "ID": b,
                   "Longitude": pixel})
#print("Original DataFrame :", df)
# Using assign() to add a 'Longitude' column
new_df = df.assign(Latitude=IDs)
#print("\nDataFrame after using assign() to add 'Latitude' column:")
print(new_df)
html_table = new_df.to_html()
#print(html_table)
with open("plot.html", "a") as f:
  f.write(html_table)
