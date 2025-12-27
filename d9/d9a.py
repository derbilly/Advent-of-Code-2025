#!/usr/bin/env python
import sys

red_tiles = []

for line in sys.stdin:
    red_tiles.append([int(val) for val in line.strip().split(',')])

area = []
for i,(x1,y1) in enumerate(red_tiles):
    for j, (x2,y2) in enumerate(red_tiles[i+1:], start=i+1):
        area.append((abs(x2-x1)+1) * (abs(y2-y1)+1))
        print(f"Pt1 ({x1},{y1})\tPt2 ({x2},{y2})\tArea: {area[-1]}")
print(f"Maximum area = {max(area)}")
