# https://www.hackerrank.com/challenges/components-in-graph/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):

    d = {}
    
    for n1, n2 in gb:
        
        if n1 not in d: d[n1] = [n2]
        else: d[n1].append(n2)
            
        if n2 not in d: d[n2] = [n1]
        else: d[n2].append(n1)
        
    max_c, min_c = 0, sys.maxsize
    
    curr_c = []
    nodes_left = set(d.keys())
    
    while nodes_left:
        
        curr_node = nodes_left.pop()
        comp = set(d[curr_node])
        stk = list(comp)
        comp.add(curr_node)
        
        while stk:
            
            node = stk.pop()
            nodes_left.remove(node)
            
            conns = d[node]
            for conn in conns:
                if conn not in comp:
                    comp.add(conn)
                    stk.append(conn)
        
        max_c = max(max_c, len(comp))
        min_c = min(min_c, len(comp))
        
    return [min_c, max_c]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
