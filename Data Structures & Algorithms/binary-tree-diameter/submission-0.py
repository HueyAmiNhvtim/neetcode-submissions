# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        visiting = deque()
        dict_node = dict()  # Map each node to its current height and diameter (sum of the height of its left and right subtree)
        dict_node[None] = (0, 0)
        visiting.appendleft(root)

        while visiting:
            node = visiting[0]

            # Add its children if it has children and said children are not processed
            if (node.left and node.left not in dict_node):
                visiting.appendleft(node.left)
            elif (node.right and node.right not in dict_node):
                visiting.appendleft(node.right)
            else: # Either node is a leaf or has all of its children processed
                node = visiting.popleft()

                # Extract diameter and height of its children
                left_diameter, left_height = dict_node[node.left]
                right_diameter, right_height = dict_node[node.right]

                # Now the node is processed, store the new diameter value and its updated height
                dict_node[node] = (max(left_height + right_height, left_diameter, right_diameter), 1 + max(left_height, right_height))

        return dict_node[root][0]
