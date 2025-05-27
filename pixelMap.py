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
b=['213.162.73.172']+b[0:lines]
#print(b)
# creating the dataframe
#df = pd.DataFrame({"IPV4": ['213.162.73.172', '109.199.115.41', #'93.37.250.70','65.183.218.91', '65.183.218.92','58.71.56.79'],
df = pd.DataFrame({"IPV4": b,
                   "City": ['Vienna', 'Dusseldorf', 'Milano','Linz', 'Milano','lines','x'],
                   "ID": ['NaN', 'NaN', 'NaN', '15.5325', 'NaN','lines','x'],
                   "Latitude": [140000, 300000, 600000, 47.0257, 600000,'lines','x']})
#print("Original DataFrame :", df)
# Using assign() to add a 'Longitude' column
new_df = df.assign(Longitude=b)
#print("\nDataFrame after using assign() to add 'Longitude' column:")
print(new_df)
html_table = new_df.to_html()
#print(html_table)
with open("plot.html", "a") as f:
  f.write(html_table)
