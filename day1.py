#!/usr/bin/python3
import sys

inputs = []
with open(sys.argv[1], 'r') as f:
    line = f.readline()
    while line:
        #print ('* ' + line, end=' ')
        mass = int(line)
        fuel = int(mass / 3) - 2
        #print ('* fuel : %d' % fuel)
        inputs.append(fuel)
        line = f.readline()

print('Part 1 : %d' %sum(inputs))

inputs = []
with open(sys.argv[1], 'r') as f:
    line = f.readline()
    while line:
        mass = int(line)
        totalmass = 0
        done = False
        while not done:
            #print ('* ' + line, end=' ')
            fuel = int(mass / 3) - 2
            #print ('* fuel : %d' % fuel)
            if fuel > 0:
                totalmass = totalmass + fuel
                mass = fuel
            else:
                done = 1
            #print ('* total mass : %d' % totalmass)
        inputs.append(totalmass)
        line = f.readline()

print('Part 2 : %d' %sum(inputs))
