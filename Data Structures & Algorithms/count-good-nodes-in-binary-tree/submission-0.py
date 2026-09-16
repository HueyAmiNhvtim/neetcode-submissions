from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 1 # The root itself is a good node
        if not root:
            return 0
        
        visiting = deque()
        visiting.appendleft((root, root.val))

        # DFS as usuals
        while visiting:
            node, max_so_far = visiting.popleft()
            if node.left: 
                if node.left.val >= max_so_far:
                    good_nodes += 1
                    visiting.appendleft((node.left, node.left.val))
                else:
                    visiting.appendleft((node.left, max_so_far))
            if node.right:
                if node.right.val >= max_so_far:
                    good_nodes += 1
                    visiting.appendleft((node.right, node.right.val))
                else:
                    visiting.appendleft((node.right, max_so_far))
        return good_nodes