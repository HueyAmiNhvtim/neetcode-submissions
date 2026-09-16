# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        visiting = deque()
        visiting.appendleft(root)

        dict_node = dict()  # Store mapping of node to its height
        dict_node[None] = 0

        while visiting:
            node = visiting[0]

            if node.left and node.left not in dict_node:
                visiting.appendleft(node.left)
            elif node.right and node.right not in dict_node:
                visiting.appendleft(node.right)
            else: # Either node is a leaf or has all of its children processed
                node = visiting.popleft()

                left_height = dict_node[node.left]
                right_height = dict_node[node.right]

                if abs(right_height - left_height) > 1:
                    return False  # Not balanced tree

                dict_node[node] = 1 + max(left_height, right_height)

        return True