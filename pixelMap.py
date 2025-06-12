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
ip_adresse1 = "46.125.249.111"  # Beispiel-IP-Adresse Vienna, Austria
geokoordinaten1 = get_geocoordinates(ip_adresse1)
for i in range(0, lines+1):
    a=str(b[i]).split("'")[1]
    b[i]=a
b=(['46.125.249.111']+b[0:lines])*5
cities=['Vocklabruck','Dusseldorf','Milan','East Cathlamet','Bothell','Mandaluyong City','Bothell']*5
bias=['0.0982°W', '0.0862°W','30.7596°W', '-168.4022°N','171.1454°N','106.4559°W','-75.621°N']*5
follower=[48.1000, 51.2215, 9.1885, -122.2054, -122.2054, 121.0410, -122.2054]*5
#for i in range(0,len(IDs)):
follower[0]=48.0167
pixel=[13.6500, 51.2215, 48.2085, -122.2054, -122.2054, 121.0410, -122.2054]*5
for i in range(0,len(pixel)):
    #pixel[i]='47.0257'
    pixel[i]=get_geocoordinates(b[i])[1]
df = pd.DataFrame({"IPV4": b,
                   "City": cities,
                   "ID": b,
                   "Longitude": pixel,
                   "Error": bias})
#print("Original DataFrame :", df)
# Using assign() to add a 'Longitude' column
new_df = df.assign(Latitude=follower)
#new_df2 = df.assign(Latitude=pixel)
#print("\nDataFrame after using assign() to add 'Latitude' column:")
print(new_df)
html_table = new_df.to_html()
#print(html_table)
with open("plot.html", "a") as f:
  f.write(html_table)
print(geokoordinaten1)
