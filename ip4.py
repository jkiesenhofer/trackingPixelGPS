import requests
def get_geocoordinates(ip_adresse):
    url = f"http://ip-api.com/json/{ip_adresse}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        return data["lat"], data["lon"]
    else:
        return None
ip_adresse1 = "213.162.73.172"  # Beispiel-IP-Adresse Vienna, Austria
ip_adresse2 = "109.199.115.41"  # Beispiel-IP-Adresse Dusseldorf, Germany

geokoordinaten1 = get_geocoordinates(ip_adresse1)
geokoordinaten2 = get_geocoordinates(ip_adresse2)
if geokoordinaten2:
    print(f"Breitengrad: {geokoordinaten2[0]}, Längengrad: {geokoordinaten2[1]}")
else:
    print("Fehler bei der Ermittlung der Geokoordinaten")
# Vienna 48°12′30.00″N 16°22′19.00″E
x1=geokoordinaten1[1]
y1=geokoordinaten1[0]
x2=geokoordinaten2[1]
y2=geokoordinaten2[0]
ip_adresse3 = "93.37.250.70"  # Beispiel-IP-Adresse Milan, Italy
geokoordinaten3 = get_geocoordinates(ip_adresse3)
x3=geokoordinaten3[1]
y3=geokoordinaten3[0]
#ip_adresse4 = "146.71.112.211"  # seed() IP-Adresse
#geokoordinaten4 = get_geocoordinates(ip_adresse4)
#x4=geokoordinaten4[1]
#y4=geokoordinaten4[0]