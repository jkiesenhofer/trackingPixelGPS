#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#                            |
#         FM-Pool            |  Optaphy: Thermoelectric Logistics Management
#          9173              |  www.optaphy.com
#                            |
#-------------------------------------------------------------------------------
#   Copyright (C) 2024 Optaphy SE
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
set nokey
set xlabel "thermal proxy power"
set ylabel "convexity"
w = "points.txt"
set terminal svg size 400,350
set output 'image.svg'
plot w using 1:2 with linespoints
