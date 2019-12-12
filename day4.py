#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    input = sys.argv[1].rstrip().split('-')
else:
    input = '248345-746315'.split('-')

begin = int(input[0])
end   = int(input[1])

print ('%d - %d' % (begin, end))

def do_meet_rule1(value):
    #print ('val %d' % value)
    has_double = False
    prev_char = ''
    for c in str(value):
        #print ('char %s, prev %s' % (c, prev_char))
        if c == prev_char:
            #print ('has double')
            has_double = True
        if prev_char != '' and int(c) < int(prev_char):
            #print ('decrease')
            return False
        prev_char = c
    return has_double

# TODO : refactor function to implement both rules
def do_meet_rule2(value):
    #print ('val %d' % value)
    found = dict()
    prev_char = ''
    prev_prev = ''
    for c in str(value):
        #print ('char %s, prev %s' % (c, prev_char))
        if c == prev_char:
            #print ('has double')
            found['%s%s' % (c, c)] = 2
        if c == prev_prev:
            found['%s%s%s' % (c, c, c)] = 3
            if '%s%s' % (c, c) in found:
                del(found['%s%s' % (c, c)])
        if prev_char != '' and int(c) < int(prev_char):
            #print ('decrease')
            return False
        prev_prev = prev_char
        prev_char = c
    for k in found:
        if found[k] == 2:
            return True
    return False

count = 0
for i in range(begin, end + 1):
    if do_meet_rule1(i):
        count += 1;

print ('Part 1 : %d' % count)

count = 0
for i in range(begin, end + 1):
    if do_meet_rule2(i):
        count += 1;

print ('Part 2 : %d' % count)
