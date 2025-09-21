"""----------------------------------------------------------------------------
-------------------------------------------------------------------------------
                            |
         FM-Pool            |  Optaphy: Thermoelectric Logistics Management
          9173              |  www.optaphy.com
                            |
-------------------------------------------------------------------------------
   Copyright (C) 2024 Optaphy SE
-------------------------------------------------------------------------------
----------------------------------------------------------------------------"""
import csv
import numpy as np
import plotly.express as px
import plotly.offline

# Initialize the 6x6 matrix of zeros
d = np.zeros((6, 6))

# Open and read the CSV file
with open('heat_map_data.csv', newline='') as f:
    reader = csv.reader(f)
    k = 0  # Row index
    for row in reader:
        # Ensure each element is a float
        c = [float(value) for value in row]  # Convert each item to float
        for i in range(len(c)):
            d[k, i] = c[i]
        k += 1

# Create the heatmap using Plotly
fig = px.imshow(d, text_auto=True)

# Show the figure (uncomment this line to view the plot inline)
#fig.show()

# Save the figure as an HTML file
plotly.offline.plot(fig, filename='temperature.html')
