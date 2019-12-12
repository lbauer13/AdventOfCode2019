#!/usr/bin/python3
import sys

def to_int(string):
    return int(string)

wire1 = []
wire2 = []
with open(sys.argv[1], 'r') as f:
    wire1 = f.readline().rstrip().split(',')
    wire2 = f.readline().rstrip().split(',')

def make_grid(wire):
    x = 0
    y = 0
    s = 0
    grid = {(x,y)}
    grid_steps = dict()
    for el in wire:
        d = el[0]
        l = int(el[1:])
        #print ('direction %s, length %d' % (d, l))
        # should have used a dictionary...
        if d == 'R':
            dx = 1
            dy = 0
        elif d == 'L':
            dx = -1
            dy = 0
        elif d == 'U':
            dx = 0
            dy = 1
        elif d == 'D':
            dx = 0
            dy = -1
        for z in range(l):
            #print ('%d, %d' % (x,y))
            x += dx
            y += dy
            s += 1
            grid.add((x,y))
            key = '%d,%d' % (x, y)
            if not key in grid_steps:
                grid_steps[key] = s
    return (grid, grid_steps)

(grid1, grid_steps1) = make_grid(wire1)
(grid2, grid_steps2) = make_grid(wire2)

min_dist = -1
for coord in grid1.intersection(grid2):
    if coord != (0,0):
        dist = abs(coord[0]) + abs(coord[1])
        if min_dist < 0 or dist < min_dist:
            min_dist = dist

print ('Part 1 : %d' % min_dist)

min_steps = -1
for coord in grid1.intersection(grid2):
    if coord != (0,0):
        steps  = grid_steps1['%d,%d' % (coord[0], coord[1])]
        steps += grid_steps2['%d,%d' % (coord[0], coord[1])]
        #print ('%d steps' % steps)
        if min_steps < 0 or steps < min_steps:
            min_steps = steps

print ('Part 2 : %d' % min_steps)
