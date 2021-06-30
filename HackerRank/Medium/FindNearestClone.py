# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
    shortest = sys.maxsize
    ends = set([i+1 for i in range(graph_nodes) if ids[i] == val])
    
    for end in ends:
        stk = [graph_to[ind] for ind,n in enumerate(graph_from) if n == end]
        stk += [graph_from[ind] for ind,n in enumerate(graph_to) if n == end]
        nxt_stk = []
        l = 1
        v = {end:True}
        
        while stk:
            curr = stk.pop(0)
            
            if curr not in v:
                v[curr] = True
                
                if curr in ends:
                    shortest = min(shortest, l)
                    break
                
                for ind, n in enumerate(graph_from):
                    if n == curr and graph_to[ind] not in v:
                        nxt_stk.append(graph_to[ind])
                    
            if not stk:
                stk = nxt_stk
                nxt_stk = []
                l += 1
        
    if shortest == sys.maxsize:
        return -1
    return shortest
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
