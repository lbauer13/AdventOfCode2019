#!/usr/bin/python3
import sys

def to_int(string):
    return int(string)

with open(sys.argv[1], 'r') as f:
    inputs = list(map(to_int, f.readline().split(',')))

orig_inputs = inputs.copy()

def compute_all(inputs, noun, verb):
    # init
    inputs[1] = noun
    inputs[2] = verb
    #print('Computing %d, %d' % (noun, verb), end = '')

    cur_pos = 0
    while True:
        if inputs[cur_pos] == 99:
            break;
        else:
            new_val1 = inputs[inputs[cur_pos+1]]
            new_val2 = inputs[inputs[cur_pos+2]]
            new_pos  = inputs[cur_pos+3]
            #print(' new val1 %d, new val2 %d, new pos %d' % (new_val1, new_val2, new_pos), end = '')
            if inputs[cur_pos] == 1:
                inputs[new_pos] = new_val1 + new_val2
            elif inputs[cur_pos] == 2:
                inputs[new_pos] = new_val1 * new_val2
        cur_pos += 4

    #print(' => %d' % inputs[0])
    return inputs

compute_all(inputs, 12, 2)
print('Part 1 : %d' % inputs[0])

searched_output = 19690720
for noun in range(100):
    for verb in range(100):
        inputs = orig_inputs.copy()
        compute_all(inputs, noun, verb)
        if inputs[0] == searched_output:
            break;
    if inputs[0] == searched_output:
        break;

print('Part 2 : %d' %(100 * noun + verb))
