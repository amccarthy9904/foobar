# https://leetcode.com/problems/clone-graph/
# 133. Clone Graph
# Medium
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Runtime 41ms Beats 61.94% of users with Python3
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        def dfs(node):
            c = Node(node.val)
            val_to_node[c.val] = c

            for n in node.neighbors:
                if n.val in val_to_node:
                    continue
                dfs(n)

            for n in node.neighbors:
                c.neighbors.append(val_to_node[n.val])
            
            return c

        val_to_node = {}
        return dfs(node)
            