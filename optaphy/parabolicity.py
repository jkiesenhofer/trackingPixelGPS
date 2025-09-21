'''----------------------------------------------------------------------------
-------------------------------------------------------------------------------
                            |
         FM-Pool            |  Optaphy: Thermoelectric Logistics Management
          9173              |  www.optaphy.com
                            |
-------------------------------------------------------------------------------
   Copyright (C) 2024 Optaphy SE
-------------------------------------------------------------------------------
----------------------------------------------------------------------------'''
r = 10
z = 0
d = '.'
b = ' '
c = lambda z: r/z
h = '*'

class Points:
    def __init__(self):
        # Printing the first row with a calculated number of stars
        print((int(c(0.08)) + 5) * h)

    def __call__(self):
        # Printing the final row with dashes
        print(cc)

# Create an instance of Points (this will print the first row of stars)
a = Points()

# Loop to generate the pattern
for x in range(int(c(0.5))):  # 20 iterations
    u = str(h + 3 * ((2 * r - x) * b + d))  # Left part of the pattern
    v = str(h + 3 * (2 * x * b) + h)  # Middle part of the pattern
    w = str(3 * (d + (2 * r - x) * b) + h)  # Right part of the pattern
    sum_pattern = u + v + w  # Combine them into a full row
    print(sum_pattern)

# Create the second pattern (dashes and stars)
s1 = (int(c(0.16)) + 2) * h
class Dashes:
    s2 = str(len(u + v + w) - 2)  # Length of the pattern minus 2 for dashes
dash = Dashes()
s3 = (int(c(0.16)) + 1) * h
cc = s1 + dash.s2 + s3  # Final string for the dashed row

# Print the second pattern (with dashes)
a = Points()  # This will print the second row of stars
for x in range(int(c(0.5))):  # Repeat the pattern generation
    u = str(h + 3 * ((2 * r - x) * b + d))  # Left part of the pattern
    v = str(h + 3 * (2 * x * b) + h)  # Middle part of the pattern
    w = str(3 * (d + (2 * r - x) * b) + h)  # Right part of the pattern
    sum_pattern = u + v + w  # Combine them into a full row
    print(sum_pattern)

# Dictionary with some arbitrary values (currently unused)
dictionary = {
    "point1": 10384,
    "point2": 10946,
    "point3": 264
}
