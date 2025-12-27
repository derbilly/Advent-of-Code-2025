#!/usr/bin/env python
import sys

def create_map(red_tiles):
    xvals, yvals = map(zip(*red_tiles))
    xmax = max(xvals)
    ymax = max(yvals)
    xmin = min(xvals)
    ymin = min(yvals)

    tile_map = [ '.'*(xmax - xmin + 3)] * (ymax - ymin + 3)

    return tile_map

def display_map(tile_map):
    pass

red_tiles = []

for line in sys.stdin:
    red_tiles.append([int(val) for val in line.strip().split(',')])

tile_map = create_map(red_tiles)
display_map(tile_map)


# area = []
# for i,(x1,y1) in enumerate(red_tiles):
    # for j, (x2,y2) in enumerate(red_tiles[i+1:], start=i+1):
        # area.append((abs(x2-x1)+1) * (abs(y2-y1)+1))
        # print(f"Pt1 ({x1},{y1})\tPt2 ({x2},{y2})\tArea: {area[-1]}")
# print(f"Maximum area = {max(area)}")
