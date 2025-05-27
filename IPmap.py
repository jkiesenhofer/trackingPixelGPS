# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import ip4 as vector
import ipaddress
import random

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES

def random_ipv4():
    return  ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, MAX_IPV4)
    )
random.seed(10)
print(random_ipv4())
# Beispiel-Daten für die Punktwolke
x = np.random.rand(10)+11.34  # (n) zufällige x-Werte um Munich
y = np.random.rand(10)+48.08  # (n) zufällige y-Werte um Munich

x[0]=vector.x1
y[0]=vector.y1
x[1]=vector.x2
y[1]=vector.y2
x[2]=vector.x3
y[2]=vector.y3

# Erstellen des Scatter-Plots
plt.scatter(x, y, c='blue', marker='o', alpha=0.5, label='Virtual IPs')

# Achsentitel und Legende hinzufügen
#plt.title('51°28'40.1"N 0°00'05.3"W for Greenwich')
#Equator x Greenwich 00°00′00.00″N 0°00′00.00″W
plt.xlabel('Latitude e.g. 16°22′19.00″E')
plt.ylabel('Longitude e.g. 48°12′30.00″N')
plt.legend()

# Plot anzeigen
plt.grid(True)
plt.show()