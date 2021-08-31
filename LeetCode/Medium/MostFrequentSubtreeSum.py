# https://leetcode.com/problems/most-frequent-subtree-sum/submissions/
# 508. Most Frequent Subtree Sum
# Medium

# Given the root of a binary tree, return the most frequent subtree sum. 
# If there is a tie, return all the values with the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values 
# formed by the subtree rooted at that node (including the node itself).




# Runtime: 44 ms, faster than 90.77% of Python3 online submissions for Most Frequent Subtree Sum.
# Memory Usage: 17.5 MB, less than 64.24% of Python3 online submissions for Most Frequent Subtree Sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        d = {} #subtree sum : freq
        
        
        def get_subtree_sum(root):
            
            if not root:
                return 0
            
            nonlocal d
            
            curr = root.val
            
            curr += get_subtree_sum(root.left)
            curr += get_subtree_sum(root.right)
            
            if curr not in d:
                d[curr] = 1
            else:
                d[curr] += 1
                
            return curr
                
        get_subtree_sum(root)
        m_freq = max(d.values())
        
        return [k for k in d.keys() if d[k] == m_freq]